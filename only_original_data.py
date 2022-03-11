import os


anno_dir = "/media/qisens/2tb1/python_projects/inference_pr/tfrecord-viewer/train/annotations_all_only_flatroof_no_seg"
string_ls = ['rotate30', 'rotate60', '0.8', '1.2']

for path, dirs, files in os.walk(anno_dir):
    for file in files:
        anno_path = os.path.join(path, file)
        file_name = os.path.splitext(file)

        for string in string_ls:
            if string in file_name[0]:
                os.remove(anno_path)
                break