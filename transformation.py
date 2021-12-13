import albumentations as A
import cv2
import os.path


class transformation():
    def __init__(self, file_path):
        self.current_path = file_path
        self.load_img_path = os.path.join(self.current_path, "dataset") 
        self.load_label_path = os.path.join(self.current_path, "dataset") 
        self.save_img_path = os.path.join(self.current_path, "dataset_aug") 
        if os.path.exists(self.save_img_path) == False:
            os.mkdir(self.save_img_path)
        self.save_label_path = os.path.join(self.current_path, "dataset_aug")
        if os.path.exists(self.save_img_path) == False:
            os.mkdir(self.save_img_path)

    '''
    def get_pixel_tf(self):
        pixel_tf = [
            A.RandomBrightnessContrast(p=0.3),
            A.RGBShift(r_shift_limit=30, g_shift_limit=30, b_shift_limit=30, p=0.3),
            A.Sharpen()
        ]
        return pixel_tf

    def get_spacial_tf(self):
        spacial_tf = [
            A.HorizontalFlip(p=0.5),
            A.ShiftScaleRotate(p=0.5),
        ]
        return spacial_tf
        '''
    def get_pixel_tf(self):
        pixel_tf = [
            A.AdvancedBlur(),
            A.Blur(),
            A.CLAHE(p=1.0), # suggested
            A.ChannelDropout(),
            A.ChannelShuffle(),
            A.ColorJitter(),
            A.Downscale(),
            A.Emboss(),
            A.Equalize(),
            #A.FDA(),
            A.FancyPCA(),
            A.FromFloat(), # white 10
            A.GaussNoise(),
            A.GaussianBlur(),
            A.GlassBlur(),
            #A.HistogramMatching(),
            A.HueSaturationValue(),
            A.ISONoise(),
            A.ImageCompression(),
            A.InvertImg(), # color negative 17
            A.MedianBlur(),
            A.MotionBlur(),
            A.MultiplicativeNoise(),
            A.Normalize(), # blacked 21
            #A.PixelDistributionAdaptation(),
            A.Posterize(),
            A.RGBShift(),
            A.RandomBrightnessContrast(),
            A.RandomFog(),
            A.RandomGamma(),
            A.RandomRain(),
            A.RandomShadow(),
            A.RandomSnow(),
            A.RandomSunFlare(),
            A.RandomToneCurve(),
            A.RingingOvershoot(),
            A.Sharpen(p=1.0), # suggested
            A.Solarize(),
            A.Superpixels(), # 뭉개짐 35
            #A.TemplateTransform(),
            A.ToFloat(), # blacked 36
            A.ToGray(),
            A.ToSepia(),
            A.UnsharpMask()
        ] # 40
        return pixel_tf
        
    def get_spacial_tf(self):
        spacial_tf = [
            A.Affine(),
            #A.CenterCrop(),
            #A.CropAndPad(),
            #A.CropNonEmptyMaskIfExists(),
            A.HorizontalFlip(),
            A.Lambda(),
            A.LongestMaxSize(),
            A.PadIfNeeded(),
            A.Perspective(),
            A.PiecewiseAffine(),
            #A.RandomCrop(),
            #A.RandomCropNearBBox(),
            #A.RandomResizedCrop(),
            A.RandomRotate90(),
            A.RandomScale(),
            #A.RandomSizedCrop(),
            #A.Resize(),
            A.Rotate(),
            A.SafeRotate(),
            A.ShiftScaleRotate(),
            A.SmallestMaxSize(),
            A.Transpose(),
            A.VerticalFlip()
        ] # 15
        return spacial_tf    

    def create_tf_list(self):
        appended_tf = []
        
        pixel_tf = self.get_pixel_tf()
        spacial_tf = self.get_spacial_tf()
        appended_tf = pixel_tf + spacial_tf
        return appended_tf


    def read_img(self, path):
        img = cv2.imread(path)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

    def read_label(self, path):
        bboxes_float_list = []
        bbox_list = []

        # label format: (class x1 y1 x2 y2), label example: 0 0.552734 0.373611 0.091406 0.027778
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
            bboxes_float_list.append(bboxes_float)    
        return bboxes_float_list

    def do_transform(self, img_path, label_path):
        save_label_path = self.save_label_path
        save_img_path = self.save_img_path
        
        bboxes = self.read_label(label_path)
        img = self.read_img(img_path)
        
        
        img_name = img_path[-11:-4]
        label_name = label_path[-11:-4]
        
        tf_list = self.create_tf_list()
        

        for idx, tf in enumerate(tf_list):
            # create transformation pipline
            transform = A.Compose(tf, bbox_params=A.BboxParams(format='yolo'))
            
            # do transform
            transformed = transform(image=img, bboxes=bboxes)

            # save transformed label data
            #transformed_category_ids = transformed['category_ids']
            transformed_bboxes = transformed['bboxes']

            # transformed_bboxes example: 
            # [(347.25, 138.95, 147.08999999999997, 164.88), (0.5000000000000004, 80.84, 132.80000000000004, 181.84)]

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
            

            save_label_dir = os.path.join(save_label_path, label_name+"_"+str(idx)+".txt")
            # save_label_path = C:/Dev/Image Augmentation/aug_dataset
            # label_name = A(0001)
            # rest = "_idx.txt"
            f = open(save_label_dir, "w")
            for i in range(len(transformed_bboxes_list_list)):
                for j in range(len(transformed_bboxes_list_list[i])):
                    f.write(transformed_bboxes_list_list[i][j] + " ")
                f.write("\n")
            f.close()
            
            # save transformed image
            transformed_image = transformed['image']
            save_img_dir = os.path.join(save_img_path, img_name+"_"+str(idx)+".jpg")
            cv2.imwrite(save_img_dir, transformed_image)

            