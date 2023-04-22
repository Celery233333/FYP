import utils
import os
import numpy as np

file_path = "D:/Celery/1/Y4/FYP/corpus/labels_note/"
output_path = "D:/Celery/1/Y4/FYP/corpus1/output/"
file_name_list1 = os.listdir(file_path)
file_name_list2 = os.listdir(output_path)

output = []
for file_name in file_name_list2:
    file1 = open(output_path+file_name,"r")
    lines1 = file1.read()

    file2 = open(file_path+file_name,"r")
    lines2 = file2.read()

    a = utils.edit_distance(lines1,lines2)
    output.append(a/len(lines2))

print(np.nanmean(output))