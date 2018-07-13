
from mnist import MNIST
import cv2
from numpy import array
from PIL import Image
import numpy as np
import pandas as pd



mndata = MNIST(r'C:\Users\sachin13390\Desktop\Samples')

images, labels = mndata.load_training()

image_Path = r'C:\Users\sachin13390\Desktop\Mnist_To_Images'
count = 1

def getResizedImage(input_Image):
    height,width = input_Image.shape
 
    number_Of_Column_To_Add = 8
    temp_Column = np.zeros( (height , int(number_Of_Column_To_Add/2)), dtype = np.uint8)
    input_Image = np.append(temp_Column, input_Image, axis=1)
    input_Image = np.append(input_Image, temp_Column, axis=1)

    height,width = input_Image.shape

    number_Of_Row_To_Add = 8
    temp_Row= np.zeros( (int(number_Of_Row_To_Add/2) , width ), dtype = np.uint8)
    input_Image = np.concatenate((temp_Row,input_Image))
    input_Image = np.concatenate((input_Image,temp_Row))

    return cv2.resize(input_Image, (28,28), interpolation = cv2.INTER_AREA )

col=[]

for i in range (785):
    if i == 0:
        col.append('label')
    else:
        col.append('pixel'+str(i-1))

df = pd.DataFrame(dtype='int', columns=col)  

file_name = r'C:\Users\sachin13390\Desktop\Mnist_To_Images_In_CSV.csv'

for index,image in enumerate(images):

    new_image_Path = image_Path + '\\' + str(labels[index])+ '\\' + str(labels[index]) + '_' + str(index+1) + '.png'
    #print (new_image_Path)
    img = array(images[index])
    img = np.resize(img,(28,28,1))
    cv2.imwrite(new_image_Path,img)
    img = cv2.imread(new_image_Path,0)
    img, contours, hire = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    Biggest_Countour = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(Biggest_Countour)
    img = getResizedImage(img[y:y+h, x:x+w])

    #cv2.imwrite(new_image_Path,img)
    img = np.append(labels[index],img)

    df.loc[index] = img

    if index % 100 == 0:
        print (index)


df.to_csv(file_name, encoding='utf-8', index=False)


