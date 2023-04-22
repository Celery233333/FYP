import os
import random

file_name_list = os.listdir("D:/Celery/1/Y4/FYP/corpus1/images")
random.seed(0)
file_name = []
for f in file_name_list:
    if f.endswith("png"):
        file_name.append(f)
random.shuffle(file_name)
# print(file_name)
# print(len(file_name))

f1 = open("D:/Celery/1/Y4/FYP/corpus1/valid.txt","a")
f2 = open("D:/Celery/1/Y4/FYP/corpus1/train.txt","a")
for i in range(len(file_name)):
    if i < int(0.2*len(file_name)):
        f1.write(file_name[i]+"\n")
    else:
        f2.write(file_name[i]+"\n")

# f = open("qc.txt","w")
# for qc in file_name:
#     f.write(qc+"\n")