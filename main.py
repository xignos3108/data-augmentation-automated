import albumentations as A
import os.path

from transformation import transformation


def main():
    file_path = os.path.dirname(os.path.abspath(__file__)) #IA folder
    dataset_path = os.path.join(file_path, "dataset")
    
    tf = transformation(file_path)
    file_list = os.listdir(dataset_path)
    tf_list = tf.create_tf_list()

    for file in file_list:
        if file.endswith('.jpg'):
            name = file[:-4] #file name without format
            img_path = os.path.join(dataset_path, name+".jpg")
            label_path = os.path.join(dataset_path, name+".txt")
        
        #img = tf.read_img(img_path)
        #label = tf.read_label(label_path)

        tf.do_transform(img_path, label_path)


if __name__== "__main__":
    main()