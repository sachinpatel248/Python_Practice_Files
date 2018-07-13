import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle

print("Start")

csv_File_Path = r'C:\Users\sachin13390\Desktop\Digits_Data\train.csv'

model_File_Path = r'C:\Users\sachin13390\Desktop\RF_Model.pkl'

df = pd.read_csv(csv_File_Path)

X = df.drop('label',axis = 1)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print(X_train.shape)
print(X_test.shape)


##Normalising the Data
##X_train = X_train/255.0
##X_test = X_test/255.0

print("RF Classify")

rf = RandomForestClassifier(n_estimators=30,verbose=3,random_state=3)
print("RF FIT MODEL")
rf.fit(X_train,y_train)

print("RF Predict")
p2 = rf.predict(X_test)


with open(model_File_Path, 'wb') as fid:
    pickle.dump(rf, fid)

    
print (classification_report(p2,y_test))
print (confusion_matrix(p2,y_test))
