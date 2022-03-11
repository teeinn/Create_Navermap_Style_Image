import cv2
import numpy as np
from add_noise import gaussian_noise, blur
import os


jp_img_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/new_data/png/test/JPEGImages"
new_img_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/new_data/png/test/naverstyle"
for path, dirs, files in os.walk(jp_img_dir):
    for file in files:
        img_path = os.path.join(path, file)
        img = cv2.imread(img_path)
        overlay_img = np.zeros(img.shape, np.uint8)
        overlay_img[:] = (28, 158, 123)

        #blur
        blur_img = blur(img)
        #noise
        noise_img = gaussian_noise(blur_img)
        #color
        colored_img = cv2.addWeighted(noise_img, 1, overlay_img, 0.08, 0)
        #sharpen
        # sharpen_filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        # sharpen_image = cv2.filter2D(colored_img, -1, sharpen_filter)

        new_img_path = os.path.join(new_img_dir, file)
        cv2.imwrite(new_img_path, colored_img)
        print(new_img_path)

