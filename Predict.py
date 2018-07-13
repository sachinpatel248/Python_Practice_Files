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

imageFilePath =r'C:\Users\Sachin13390\Desktop\Forms\InputImage5.jpg'

x = 850
y = 1150
w = 300
h = 70

x = 1950
y = 1045
w = 450
h = 70

x = 800
y = 3215
w = 450
h = 75

x = 'YASHPALSHJNDE'
x = 800
y = 1050
w = 650
h = 65

##x = 'SACH[T,Y]NAHER'
##x = 1000
##y = 2100
##w = 550
##h = 80

##x = "DEVELOPME[N,H]T"
##x = 1980
##y = 1175
##w = 500
##h = 50

##x = "DUE to his skills"
x = 1375
y = 2670
w = 1300
h = 70

####x = 'KEPTONHOLD'
##x = 790
##y = 3320
##w = 625
##h = 85

####x = 'BAYNOCDKP'
##x = 770
##y = 1760
##w = 1170
##h = 110

####x = 'DEVEWPMENT'
##x = 1050
##y = 2400
##w = 510
##h = 90

####x = "Image 4"
##x = 1170
##y = 2130
##w = 850
##h = 100

Alphabet_Mapping_List = list(string.ascii_uppercase)


NN_model_File_Path = r'C:\Users\sachin13390\Desktop\NN_Model.pkl'
RF_model_File_Path = r'C:\Users\sachin13390\Desktop\NN_Model.pkl'
KERAS_model_File_Path = r'C:\Users\sachin13390\Desktop\KERAS_MODEL.h5'
KERAS_Alphabet_model_File_Path = r'C:\Users\sachin13390\Desktop\Keras_Alphabet_Model.h5'

image = cv2.imread(imageFilePath)

kernel = np.ones((3,3),np.uint8)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray_image,(5,5),0)
ret3,Otsu_Threshold_GaussianBlur_Image = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
Otsu_Threshold_GaussianBlur_Image = cv2.bitwise_not(Otsu_Threshold_GaussianBlur_Image)


closing = cv2.morphologyEx(Otsu_Threshold_GaussianBlur_Image, cv2.MORPH_CLOSE, kernel)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\closing.jpg',closing)


cropped_im =closing[y:y+h, x:x+w]
cropped_im = cv2.morphologyEx(cropped_im, cv2.MORPH_CLOSE, kernel)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\cropped_im.jpg',cropped_im)


im2, contours, hierarchy = cv2.findContours(cropped_im, cv2.RETR_EXTERNAL
                                            , cv2.CHAIN_APPROX_SIMPLE)
#print (type(cropped_im))

##for cnt in contours:
##    x,y,w,h = cv2.boundingRect(cnt)
##    cv2.rectangle(cropped_im,(x,y),(x+w,y+h),(255,0,0),1)
##cv2.imwrite(r'C:\Users\sachin13390\Desktop\croppedrect.jpg',cropped_im)



try:
##    with open(RF_model_File_Path, 'rb') as rf_model:
##        RF_Model = pickle.load(rf_model);
##    with open(NN_model_File_Path, 'rb') as nn_model:
##        NN_Model = pickle.load(nn_model);
##
##    KERAS_Model = load_model(KERAS_model_File_Path)
    KERAS_Alphabet_Model = load_model(KERAS_Alphabet_model_File_Path)
except:
    
    KERAS_Model = load_model(KERAS_model_File_Path)




count = 1

boundingBoxes = [cv2.boundingRect(c) for c in contours]
(contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes),
		key=lambda b:b[1][0], reverse=False))

def getResizedImage(input_Image, Image_Size):
    height,width = input_Image.shape
    
    number_Of_Column_To_Add = 28
    temp_Column = np.zeros( (height , int(number_Of_Column_To_Add/2)), dtype = np.uint8)
    input_Image = np.append(temp_Column, input_Image, axis=1)
    input_Image = np.append(input_Image, temp_Column, axis=1)

    height,width = input_Image.shape


    number_Of_Row_To_Add = 28
    temp_Row= np.zeros( (int(number_Of_Row_To_Add/2) , width ), dtype = np.uint8)
    input_Image = np.concatenate((temp_Row,input_Image))
    input_Image = np.concatenate((input_Image,temp_Row))

    return cv2.resize(input_Image, (Image_Size,Image_Size), interpolation = cv2.INTER_AREA )


def getNewResizedImage(input_Image, Image_Size):
    height,width = input_Image.shape
    #print (height, width)

    if width > height:
        aspect_Ratio = (float)(width/height)
        width = 20
        height = round(width/aspect_Ratio)
    else:
        aspect_Ratio = (float)(height/width)
        height = 20
        width = round(height/aspect_Ratio)
		
##    path = r'C:\Users\sachin13390\Desktop\\' + 'z'+'.png'
##    cv2.imwrite(path,cv2.resize(input_Image, (Image_Size,Image_Size), interpolation = cv2.INTER_AREA))
    input_Image = cv2.resize(input_Image, (width,height), interpolation = cv2.INTER_AREA )
    
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

    return cv2.resize(input_Image, (Image_Size,Image_Size), interpolation = cv2.INTER_AREA )




RF_Prediction = ''
NN_Prediction = ''
KERAS_Prediction = ''
KERAS_Alphabet_Prediction = ''
temp_Index = ''

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)

    if w > 5 and h > 10:

        resize_image = getNewResizedImage(cropped_im[y:y+h, x:x+w] , 28)
        path = r'C:\Users\sachin13390\Desktop\\' + str(count)+'.png'
        cv2.imwrite(path,resize_image)
        resize_image = resize_image.flatten()
        count = count + 1

        #RF_Prediction = RF_Prediction + str(RF_Model.predict(resize_image.reshape(1,-1)))
        #NN_Prediction = NN_Prediction + str(NN_Model.predict(resize_image.reshape(1,-1)))
        #KERAS_Prediction = KERAS_Prediction + str(KERAS_Model.predict_classes(resize_image.reshape(1,784)/255.0))
        temp_Index = int(KERAS_Alphabet_Model.predict_classes(resize_image.reshape(1,784)/255.0)[0])
        alphabet_probability = (KERAS_Alphabet_Model.predict_proba(resize_image.reshape(1,784)/255.0))
        sort_alphabet_probability = -np.sort(-alphabet_probability)
        if sort_alphabet_probability[0,0] > 0.99:
            KERAS_Alphabet_Prediction = KERAS_Alphabet_Prediction + Alphabet_Mapping_List[int(temp_Index)]
        else:
            alternate_Probable_Alphabet = Alphabet_Mapping_List[int(np.where(alphabet_probability == sort_alphabet_probability[0,1])[1][0])]
            KERAS_Alphabet_Prediction = KERAS_Alphabet_Prediction + "[" + Alphabet_Mapping_List[int(temp_Index)] + "," + alternate_Probable_Alphabet + "]"
            


print('RF_Prediction          ' + RF_Prediction)
print('NN_Prediction          ' + NN_Prediction)
print('KERAS_Predict          ' + KERAS_Prediction)
print ('')
print('KERAS_Alphabet_Predict ' + KERAS_Alphabet_Prediction)

cv2.destroyAllWindows()
