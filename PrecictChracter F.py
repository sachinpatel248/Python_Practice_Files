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
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'


KERAS_Alphabet_model_File_Path = r'C:\Users\sachin13390\Desktop\Keras_Alphabet_Model.h5'


source_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\relevant data'

irrevelant_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\TempFolder of irrevelant data'

F_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\temp F'
Alphabet_Mapping_List = list(string.ascii_uppercase)


KERAS_Alphabet_Model = load_model(KERAS_Alphabet_model_File_Path)


def getNewResizedImage(input_Image):
    height,width = input_Image.shape
    #print (height, width)
    input_Image = cv2.resize(input_Image, (20,20), interpolation = cv2.INTER_AREA )

    height,width = input_Image.shape    

    number_Of_Column_To_Add = 28-width
    temp_Column = np.zeros( (height , int(number_Of_Column_To_Add/2)), dtype = np.uint8)
    input_Image = np.append(temp_Column, input_Image, axis=1)
    input_Image = np.append(input_Image, temp_Column, axis=1)


    height,width = input_Image.shape

    number_Of_Row_To_Add = 28-height
    temp_Row= np.zeros( (int(number_Of_Row_To_Add/2) , width ), dtype = np.uint8)
    input_Image = np.concatenate((temp_Row,input_Image))
    input_Image = np.concatenate((input_Image,temp_Row))

    return cv2.resize(input_Image, (28,28), interpolation = cv2.INTER_AREA )






image_Total_Pixels = 28*28

count = 0
kernel = np.ones((3,3),np.uint8)
KERAS_Alphabet_Prediction = ''

for root, dirs, files in os.walk(source_Image_Folder_Path):
    for filename in files:
        image_Path = (os.path.join(root,filename))
        image  =  cv2.imread(image_Path,0)
        image = getNewResizedImage(image)

        white_pixels_Count = 0

        for pixelValue in np.nditer(image):
            if pixelValue > 155:
                white_pixels_Count = white_pixels_Count + 1

        if white_pixels_Count < (int)(0.15 * image_Total_Pixels):
            image = cv2.dilate(image, kernel, iterations=5)

        temp_Index = int(str(KERAS_Alphabet_Model.predict_classes(image.reshape(1,784)/255.0)).replace("[", "").replace("]", ""))
        KERAS_Alphabet_Prediction + Alphabet_Mapping_List[int(temp_Index)]

        filename =  str(count) + '.png'
        print (os.path.join(F_Image_Folder_Path,filename))
        print (os.path.join(irrevelant_Image_Folder_Path,filename))
            

        if (KERAS_Alphabet_Prediction == 'F'):
            shutil.move(image_Path, os.path.join(F_Image_Folder_Path,filename))
        elif():
            shutil.move(image_Path, os.path.join(irrevelant_Image_Folder_Path,filename))

        count = count + 1
        if count % 10==0:
            print (count)






