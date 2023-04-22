import os

file_name_list = os.listdir("C:/Users/Celery/Desktop/corpus/labels")
temp = []        
for f in file_name_list:
    if f.endswith("semantic"):
        file = open("C:/Users/Celery/Desktop/corpus/labels"+"/"+f,"r")
        label = file.read()
        array = label.split(" ")
        for note in array:
            print(note)
            if note.find("_"):
                temp.append("note-"+note.split("_")[-1])
            else:
                temp.append(note)
        string = " ".join(temp)
        temp = []
        note_file=open("C:/Users/Celery/Desktop/corpus/2"+"/"+f,'w')   
        note_file.write(string)