import os

file_name = "D:/Celery/1/Y4/FYP/corpus1/label"
file_name_list = os.listdir(file_name)
temp = []
for f in file_name_list:
    if f.endswith("semantic"):
        file = open(file_name+"/"+f,"r")
        label = file.read()
        array = label.split(" ")
        for note in array:
            if note.startswith("note"):
                note = note.split("_")[0]
                note = note.replace("N","")
                temp.append(note)
            else:
                temp.append(note)
        string = " ".join(temp)
        temp = []
        note_file=open("D:/Celery/1/Y4/FYP/corpus1/labels_note"+"/"+f,'w')   
        note_file.write(string)

temp = []        
for f in file_name_list:
    if f.endswith("semantic"):
        file = open(file_name+"/"+f,"r")
        label = file.read()
        array = label.split(" ")
        for note in array:
            if note.startswith("note"):
                temp.append("note-"+note.split("_")[1])
            else:
                temp.append(note)
        string = " ".join(temp)
        temp = []
        note_file=open("D:/Celery/1/Y4/FYP/corpus1/labels_length"+"/"+f,'w')   
        note_file.write(string)