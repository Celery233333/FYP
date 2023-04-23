import pandas as pd
import numpy as np
import missingno
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
import tensorflow.keras.models


def changeNote(o):
    dict = {
        'C': 1,
        'D': 2,
        'E': 3,
        'F': 4,
        'G': 5,
        'A': 6,
        'B': 7}
    return dict.get(o)

def changeKey(o):
    dict = {
        'CM':[14, 20, 33, 4, 29, 25, 27, 12, 31, 13, 28, 32],
        'EM':[0, 21, 6, 1],
        'GM':[14, 33, 4, 16, 25, 12, 9, 31, 13, 17, 34, 32],
        # 'GM':[14, 33, 4, 16, 25, 12, 9, 31, 13, 17, 34, 32],
        'AM':[16, 0, 21, 9, 1, 17],
        'BM':[21, 6],
        'DM':[33, 16, 0, 25, 9, 31, 1, 17, 34, 32],
        'FM':[14, 20, 35, 4, 8, 29, 27, 12, 13, 28, 26, 7],
        'AbM':[23, 15, 3, 19, 9, 30, 22, 2],
        'BbM':[20, 35, 8, 29, 15, 27, 28, 7, 5],
        'DbM':[3, 19, 9, 30, 24, 2, 18],
        # 'EbM':[35, 8, 23, 15, 3, 30, 22, 7, 2],
        'EbM':[35, 8, 23, 15, 3, 30, 22, 7, 2]
    }
    return dict.get(o)

def predict_chord(path, level):
    try:
        df = pd.read_csv(path, na_values="noNote")
        df.drop(['file'], axis=1, inplace=True)
        df.drop(['note7','note8','note9','note10'], axis=1, inplace=True)
    except:
        return ''

    # delete = set()
    # for i in range(len(df)):
    #     mykey = df['keySignature'][i]  
    #     if not isinstance(mykey,str):
    #         delete.add(i)

    scaler = 1
    for i in range(1,7):
        category = 'note' + str(i)
        for n in range(len(df)):
            note = df[category][n]
            
            if isinstance(note,str):
                if "note" not in note:
                    df[category][n] = np.NAN
                else:
                    myNote = note.split("-")[1]
                    if len(myNote) == 2:
                        num = changeNote(myNote[0])
                        df[category][n] = num*scaler + 7*(int(myNote[1])-1)*scaler
                    if len(myNote) == 3:
                        num1 = changeNote(myNote[0])
                        if myNote[1] == 'b':
                            num2 = -0.49
                        else:
                            num2 = 0.49
                        df[category][n] = num1*scaler + 7*(int(myNote[2])-1)*scaler + num2*scaler

    le1 = joblib.load('models/chord.pkl')
    le2 = joblib.load('models/key.pkl')

    try:
        keys = df['keySignature']
    except:
        return '&'
    for i in range(len(keys)):
        df['keySignature'][i] = keys[i].strip()
    df['keySignature'] = le2.transform(df['keySignature'])

    imputer = joblib.load('models/KNN.pkl')
    imputed = imputer.transform(df)
    df = pd.DataFrame(imputed, columns=df.columns)
    # df = pd.DataFrame(imputed, columns=df.columns)

    df.to_csv("qc.csv", encoding='utf-8')

    predictors = df.iloc[:,0:119]


    ss = joblib.load('models/norm.pkl')
    predictors_norm = ss.transform(predictors)
    predictors_norm = predictors_norm[:-1]

    model = tensorflow.keras.models.load_model('models/model.h5')
    try:
        y_predicted = model.predict(predictors_norm)
    except:
        return '&'
    final_predicted = np.argmax(y_predicted, axis=1, out=None)

    # model = joblib.load('models/Rec.pkl')
    # y_predicted = model.predict(predictors_norm)
    # final_predicted = y_predicted
    # for i in range(len(y_predicted)):
    #     final_predicted[i] = int(y_predicted[i])
    # print(final_predicted)

    chord_predicted = le1.inverse_transform(final_predicted)

    if level != 0:
        print(len(chord_predicted))
        for i in range(len(chord_predicted)):
            if level == 5:
                t = 0.5
            if level == 10:
                t = 0.55
            if level == 15:
                t = 0.6
            if level == 20:
                t = 0.7
            if level == 25:
                t = 0.75
            if level == 30:
                t = 0.8
            if max(y_predicted[i]) < t:
                ambiguity = y_predicted[i].argsort()[-4:][::-1]
                key_chord = changeKey(keys[i].strip())
                for j in range(len(ambiguity[1:])):
                            if ambiguity[1:][j] in key_chord:
                                ambiguity = np.insert(ambiguity, 1, ambiguity[1:][j])
                                ambiguity = np.delete(ambiguity, j+2)

                hehe = ''
                for j in le1.inverse_transform(ambiguity):
                    hehe += str(j)+','
                
                chord_predicted[i] = hehe[:-1]

    return chord_predicted