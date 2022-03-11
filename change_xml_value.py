import os
import cv2
import xml.etree.ElementTree as ET

total_path = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/output_new_bk/rotate/"
folder_ls = [dirs for path, dirs, files in os.walk(total_path)][0]
for folder in folder_ls:
    img_dir = total_path + folder + "/train/JPEGImages"
    anno_dir = total_path + folder + "/train/annotations"


# img_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/train/JPEGImages_bk"
# anno_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/train/annotations_bk"
    cnt = 0

    for path, dirs, files in os.walk(img_dir):
        for file in files:
            file_path = os.path.join(path, file)
            im = cv2.imread(file_path)
            size = im.shape
            new_height, new_width = str(size[0]), str(size[1])

            anno_path = file_path.replace("JPEGImages", "annotations").replace("png", "xml")
            if os.path.exists(anno_path):
                cnt += 1
                print("cnt:{}".format(cnt))

                doc = ET.parse(anno_path)
                root = doc.getroot()
                obj_tag = root.findall("size")
                width = (obj_tag[0].find("width").text)
                height = (obj_tag[0].find("height").text)

                if width != new_width and height != new_height:
                    print(anno_path)
                    obj_tag[0].find("width").text = new_width
                    obj_tag[0].find("height").text = new_height
                    doc.write(anno_path)

