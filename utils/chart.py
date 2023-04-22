import os
import pandas as pd

file_name_list = os.listdir("D:/Celery/1/Y4/FYP/corpus1/output")
df = pd.DataFrame({"file":[], "keySignature":[], "note1":[], "note2":[], "note3":[], "note4":[]
, "note5":[], "note6":[], "note7":[], "note8":[], "note9":[], "note10":[]})        
for f in file_name_list:
    if f.endswith("semantic"):
        file = open("D:/Celery/1/Y4/FYP/corpus1/output"+"/"+f,"r")
        print(f)
        label = file.read()
        array = label.split("+")
        key = "noNote"
        for note in array:
            harmony = ["noNote","noNote","noNote","noNote","noNote","noNote","noNote","noNote","noNote","noNote"]
            if "note" in note:
                note = note.strip()
                #print(note)
                individual = note.split(" ")
                length = len(individual)
                if length >= 3:
                    for i in range(length):
                        harmony[i] = individual[i]
                    
                    df1 = pd.DataFrame({"file":[f], "keySignature":[key], "note1":[harmony[0]], "note2":[harmony[1]], 
                    "note3":[harmony[2]], "note4":[harmony[3]], "note5":[harmony[4]], "note6":[harmony[5]],
                    "note7":[harmony[6]], "note8":[harmony[7]], "note9":[harmony[8]], "note10":[harmony[9]]})
                    df = pd.concat([df,df1])
                    #print(harmony)
                    #print("11111111111111111111")

            if "keySignature" in note:
                key = note.split("-")[1]
        #print("1111111111111111")
        df1 = pd.DataFrame({"file":[1], "keySignature":[1], "note1":[1], "note2":[1], "note3":[1], "note4":[1],
        "note5":[1], "note6":[1], "note7":[1], "note8":[1], "note9":[1], "note10":[1]})
        df = pd.concat([df,df1])
         

df.to_csv("harmony.csv",index=False)