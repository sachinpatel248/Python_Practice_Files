from  scipy import ndimage
import math
import numpy as np
import argparse
import cv2
from math import atan2, pi
import string
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
from keras.models import Sequential, load_model
import os
import shutil
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'


KERAS_Alphabet_model_File_Path = r'C:\Users\sachin13390\Desktop\Keras_Alphabet_Model.h5'


CharacterToConsider = 'Z'

source_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\A_Z HandwrittenData\\'+CharacterToConsider

irrevelant_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\B'

F_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\A'
Alphabet_Mapping_List = list(string.ascii_uppercase)

KERAS_Alphabet_Model = load_model(KERAS_Alphabet_model_File_Path)

image_Total_Pixels = 28*28

count = 0
kernel = np.ones((3,3),np.uint8)
KERAS_Alphabet_Prediction = ''

for root, dirs, files in os.walk(source_Image_Folder_Path):
    for filename in files:
        image_Path = (os.path.join(root,filename))
        image  =  cv2.imread(image_Path,0)

        temp_Index = int(str(KERAS_Alphabet_Model.predict_classes(image.reshape(1,784)/255.0)).replace("[", "").replace("]", ""))
        KERAS_Alphabet_Prediction = Alphabet_Mapping_List[int(temp_Index)]
        #print (KERAS_Alphabet_Prediction)

        
        #print (os.path.join(F_Image_Folder_Path,filename))
        #print (os.path.join(irrevelant_Image_Folder_Path,filename))
            

        if not (KERAS_Alphabet_Prediction == CharacterToConsider):
            #cv2.imwrite(os.path.join(F_Image_Folder_Path,filename),image)
            filename =  KERAS_Alphabet_Prediction+ '__' + str(count) + '.png'
            shutil.move(image_Path, os.path.join(F_Image_Folder_Path,filename))
##        if (KERAS_Alphabet_Prediction == 'U'):
##            #cv2.imwrite(os.path.join(irrevelant_Image_Folder_Path,filename),image)
##            shutil.move(image_Path, os.path.join(irrevelant_Image_Folder_Path,filename))

        count = count + 1
        if count % 100==0:
            print (count)






