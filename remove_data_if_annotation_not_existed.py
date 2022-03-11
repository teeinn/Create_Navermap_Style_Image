import os
import shutil

# img_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/train/train/JPEGImages"
# anno_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/train/train/annotations"
# #
# for path, dirs, files in os.walk(img_dir):
#     for file in files:
#         img_path = os.path.join(path, file)
#         file_name = file.split('.png')
#         anno_name = file_name[0]+'.xml'
#         anno_path = os.path.join(anno_dir, anno_name)
#
#         if not os.path.exists(anno_path):
#             print(anno_path)
#             os.remove(img_path)



# anno_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/test/test/annotations"
# string_ls = ['rotate30', 'rotate60', '0.8', '1.2']
#
# for path, dirs, files in os.walk(anno_dir):
#     for file in files:
#         anno_path = os.path.join(path, file)
#         file_name = os.path.splitext(file)
#
#         for string in string_ls:
#             if string in file_name[0]:
#                 os.remove(anno_path)
#                 break


img_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/train/JPEGImages"
anno_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/test/annotations_new"
new_save_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/test/JPEGImages_new"
#
for path, dirs, files in os.walk(anno_dir):
    for file in files:
        anno_path = os.path.join(path, file)
        file_name = file.split('.xml')
        img_name = file_name[0]+'.png'
        img_path = os.path.join(img_dir, img_name)

        if os.path.exists(img_path):
            print(img_path)
            shutil.copy(img_path, new_save_dir)