
import os
import shutil

# blur_dir = "/media/qisens/2tb1/python_projects/training_pr/R2CNN_Faster_RCNN_Tensorflow/data/io/output_new_bk/train/original_resize1.2"
#
# for path, dirs, files in os.walk(blur_dir):
#     for file in files:
#         old_file_path = os.path.join(path, file)
#         file_ls = os.path.splitext(file)
#         # new_file_name = file_ls[0].replace("_blur", "") + file_ls[1]
#         new_file_name = file_ls[0] + "_1.2" + file_ls[1]
#         new_file_path = os.path.join(path, new_file_name)
#
#         # shutil.copy(old_file_path, new_file_path)
#         os.rename(old_file_path, new_file_path)




blur_dir = "/media/qisens/2tb1/python_projects/training_pr/json"

for path, dirs, files in os.walk(blur_dir):
    for file in files:
        file_name, ext = os.path.splitext(file)
        if ext == '.xml':
            new_name = file_name + '.json'

            old_file_path = os.path.join(path, file)
            new_file_path = os.path.join(path, new_name)

            print(new_file_path)
            os.rename(old_file_path, new_file_path)