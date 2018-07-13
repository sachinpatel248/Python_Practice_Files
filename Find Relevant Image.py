import numpy as np
import pandas as pd
import os
import cv2
import shutil


source_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\relevant data'

Destination_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\TempFolder of irrevelant data'

root, dirs, files = os.walk(source_Image_Folder_Path).next()

image_Total_Pixels = 28*28

count = 0

listIntensityImages = []

for filename in files:
    image_Path = (os.path.join(root,filename))
    #print (image_Path)
    image  =  cv2.imread(image_Path,0).reshape(1,784)
    #print type(image)

    black_pixels_Count = 0
    white_pixels_Count = 0

    for pixelValue in np.nditer(image):
        #print (pixelValue)
        if pixelValue > 155:
            white_pixels_Count = white_pixels_Count + 1
##        elif pixelValue < 40:
            
##            black_pixels_Count = black_pixels_Count + 1
##    stringIntensity = str(white_pixels_Count)+'@'+str(image_Path)
##    listIntensityImages.append(stringIntensity)

    if white_pixels_Count > (int)(0.25 * image_Total_Pixels):# or white_pixels_Count < (int)(0.1 * image_Total_Pixels):
        shutil.move(image_Path, os.path.join(Destination_Image_Folder_Path,filename))
        count = count + 1
        if count%10==0:
            print (count)

##print len(listIntensityImages)
##print type(listIntensityImages)
##
##listIntensityImages.sort(reverse=True)
##
##count = 111111111111
##
##for imag in listIntensityImages:
##    x,source_image_Path = imag.split("@")
##    filename = str(count) + '.png'
###    print imag
###    print os.path.join(Destination_Image_Folder_Path,filename)
##    shutil.move(source_image_Path, os.path.join(Destination_Image_Folder_Path,filename))
##    count = count + 1
##    if count % 100==0:
##        print count
##        

    
    








