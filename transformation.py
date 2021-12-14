import albumentations as A
import cv2
import os.path

from configs import PIP_CONFIGS

class transformation():
    def __init__(self, file_path):
        self.current_path = file_path
        self.load_img_path = os.path.join(self.current_path, "dataset") 
        self.load_label_path = os.path.join(self.current_path, "dataset") 
        self.save_img_path = os.path.join(self.current_path, "dataset_augmented") 
        if os.path.exists(self.save_img_path) == False:
            os.mkdir(self.save_img_path)
        self.save_label_path = os.path.join(self.current_path, "dataset_augmented")
        if os.path.exists(self.save_img_path) == False:
            os.mkdir(self.save_img_path)

  
    def get_tf_list(self):
        appended_tf = []
        configs = PIP_CONFIGS
        
        pixel_tf = configs['PIXEL_TF'] 
        spacial_tf = configs['SPACIAL_TF']
        appended_tf = pixel_tf + spacial_tf
        return appended_tf

    def read_img(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

    def read_label(self, path):
        bboxes_float_list = []
        bbox_list = []

        # label format: (class x1 y1 x2 y2) 
        # label example: 0 0.552734 0.373611 0.091406 0.027778
        f = open(path, "r")
        while True:
            line = f.readline()
            if not line: break
            bboxes = line.split()
            bboxes.append(bboxes[0])
            del bboxes[0]
            bbox_list.append(bboxes)
        f.close

        # bbox formatted into (x1 y1 x2 y2 class)
        for i in range(len(bbox_list)):
            bboxes_float = []
            for j in range(4):
                bbox_float = float(bbox_list[i][j])
                bboxes_float.append(bbox_float)
            bboxes_float.append(bbox_list[i][4])
            
            bbox_x1 = 2*bboxes_float[0]-bboxes_float[2]
            bbox_y1 = 2*bboxes_float[1]-bboxes_float[3]
            bbox_x2 = 2*bboxes_float[0]+bboxes_float[2]
            bbox_y2 = 2*bboxes_float[1]+bboxes_float[3]
            if (bbox_x1<0.0 and bbox_x1>1.0 
            and bbox_y1<0.0 and bbox_y1>1.0 
            and bbox_x2<0.0 and bbox_x2>1.0
            and bbox_y2<0.0 and bbox_y2>1.0):
                continue
            bboxes_float_list.append(bboxes_float)    
        return bboxes_float_list


    def do_transform(self, img_path, label_path):
        configs = PIP_CONFIGS
        save_label_path = self.save_label_path
        save_img_path = self.save_img_path
        
        label_name = label_path[-11:-4] 
        img_name = img_path[-11:-4]
        
        bboxes = self.read_label(label_path)
        img = self.read_img(img_path)
        
        tf_default_list = configs['DEFAULT_TF']
        tf_list = self.get_tf_list()

        for idx, tf in enumerate(tf_list):
            ## check if the file already exists
            save_label_dir = os.path.join(save_label_path, label_name+"_"+str(idx)+".txt")
            save_img_dir = os.path.join(save_img_path, img_name+"_"+str(idx)+".jpg")
            if os.path.exists(save_label_dir) == True:
                continue
            else:
                ## create transformation pipline
                tf_pipline = []
                for d_tf in tf_default_list:
                    tf_pipline.append(d_tf)
                tf_pipline.append(tf)
                transform = A.Compose(tf_pipline, bbox_params=A.BboxParams(format='yolo'))
                
                ## do transform
                transformed = transform(image=img, bboxes=bboxes)

                ## save transformed label data
                #transformed_category_ids = transformed['category_ids']
                transformed_bboxes = transformed['bboxes']

                # transformed_bboxes is 'tuple in list' structure 
                transformed_bboxes_list_list = []
                for i in range (len(transformed_bboxes)):
                    transformed_bboxes_list = []      
                    transformed_bboxes_list.append(str(transformed_bboxes[i][-1])) # class
                    transformed_bboxes_list.append(str(round(transformed_bboxes[i][0], 6)))
                    transformed_bboxes_list.append(str(round(transformed_bboxes[i][1], 6)))
                    transformed_bboxes_list.append(str(round(transformed_bboxes[i][2], 6)))
                    transformed_bboxes_list.append(str(round(transformed_bboxes[i][3], 6)))
                    transformed_bboxes_list_list.append(transformed_bboxes_list)
                
                # save_label_path = C:/Dev/Image Augmentation/aug_dataset
                # label_name = A(0001)
                # rest = "_idx.txt"
                f = open(save_label_dir, "w")
                for i in range(len(transformed_bboxes_list_list)):
                    for j in range(len(transformed_bboxes_list_list[i])):
                        f.write(transformed_bboxes_list_list[i][j] + " ")
                    f.write("\n")
                f.close()
                
                ## save transformed image
                transformed_image = transformed['image']
                transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR)
                cv2.imwrite(save_img_dir, transformed_image)