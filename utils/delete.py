import os

name = 'C:/Users/Celery/Desktop/image'
file_name_list = os.listdir(name)
count = 1
for f in file_name_list:
    if f.endswith("musicxml"):
        os.remove(name+'/'+f)
    # if f.endswith("musicxml"):
    #     os.rename(name+'/'+f,name+'/'+str(count)+'.musicxml')
    #     count += 1

