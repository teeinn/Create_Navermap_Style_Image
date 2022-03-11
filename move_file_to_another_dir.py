import os
import shutil
import cv2
import xml.etree.ElementTree as ET

original_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/output/train/JPEGImages_original"
new_dir = "/media/qisens/2tb1/python_projects/inference_pr/naver_greenizing_project/tokyo_file/gangnam/original"
new_save_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/output/train/JPEGImages_sharp"

for path, dirs, files in os.walk(original_dir):
    for file in files:
        filename, ext = os.path.splitext(file)
        new_file_path = filename + '.png'

        for path, dirs, files in os.walk(new_dir):
            for file in files:
                if file == new_file_path:
                    img_path = os.path.join(path, file)
                    shutil.copy(img_path, new_save_dir)


# original_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/train/annotations_original"
# new_img_save_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/test/JPEGImages"
# new_anno_save_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/test/annotations"
#
# for path, dirs, files in os.walk(original_dir):
#     for file in files:
#         folder_ls = path.split('/')
#         if folder_ls[-1] == "JPEGImages":
#             file_path = os.path.join(path, file)
#             new_file_path = os.path.join(new_img_save_dir, file)
#             shutil.move(file_path, new_file_path)
#
#         if folder_ls[-1] == "annotations":
#             file_path = os.path.join(path, file)
#             new_file_path = os.path.join(new_anno_save_dir, file)
#             shutil.move(file_path, new_file_path)

# original_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/train/annotations_original"
# new_img_save_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/train/JPEGImages_origin"
#
# for path, dirs, files in os.walk(original_dir):
#     for file in files:
#         folder_ls = path.split('/')
#         if folder_ls[-1] == "JPEGImages":
#             file_path = os.path.join(path, file)
#             new_file_path = os.path.join(new_img_save_dir, file)
#             shutil.move(file_path, new_file_path)
#
#         if folder_ls[-1] == "annotations":
#             file_path = os.path.join(path, file)
#             new_file_path = os.path.join(new_anno_save_dir, file)
#             shutil.move(file_path, new_file_path)



