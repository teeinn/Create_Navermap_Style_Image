import cv2
import numpy as np
import os

dir_path = "/media/qisens/2tb1/python_projects/training_pr/Scribble_Training_Project/pytorch/pytorch-deeplab_v3_plus/inference_test_img_seochogu_large (copy 1)"
sharpening_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

for path, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(dir_path, file)
        image = cv2.imread(file_path)
        dst = cv2.filter2D(image, -1, sharpening_1)
        cv2.imwrite(file_path, dst)
        print(file_path)
