import numpy as np
import pandas as pd
import os
import cv2
import shutil


source_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\relevant data'

Destination_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\F'

root, dirs, files = os.walk(source_Image_Folder_Path).next()

image_Total_Pixels = 28*28

count = 0

listIntensityImages = []


def getNewResizedImage(input_Image):
		
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

i = 0
kernel = np.ones((3,3),np.uint8)

for filename in files:
    image_Path = (os.path.join(root,filename))
    image  =  cv2.imread(image_Path,0).reshape(1,784)
    count = count + 1

    black_pixels_Count = 0
    white_pixels_Count = 0

    pixelindex = 0
    for pixelValue in np.nditer(image):
        if pixelValue > 180:
            white_pixels_Count = white_pixels_Count + 1
            
        if pixelValue > 70 and pixelValue < 200:
            image[0,pixelindex] = pixelValue+45
        pixelindex = pixelindex + 1

    image = image.reshape(28,28)
    
    if white_pixels_Count < (int)(0.14 * image_Total_Pixels):
        i=1
        image = cv2.dilate(image, kernel, iterations=1)
##        image = getNewResizedImage(image)
##        cv2.imwrite(os.path.join(Destination_Image_Folder_Path,filename), image)
##        
    if white_pixels_Count > (int)(0.30 * image_Total_Pixels):
        image = cv2.erode(image, kernel, iterations=1)
##        image = getNewResizedImage(image)
##        cv2.imwrite(os.path.join(Destination_Image_Folder_Path,filename), image)

    image = getNewResizedImage(image)

    cv2.imwrite(os.path.join(Destination_Image_Folder_Path,filename), image)
             

    if count % 100 == 0:
        print (count)




