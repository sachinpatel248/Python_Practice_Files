import cv2
import os
import numpy as np
import nltk


imageName = 'A'

source_Image_Path = r'C:\Users\sachin13390\Desktop\Temp Capital F'

destination_Image_Path = r'C:\Users\sachin13390\Desktop\F'


dirnames = os.listdir(source_Image_Path)


print ('')
print (imageName)
print ('')


number = 1000000000

def getNewResizedImage(input_Image, Image_Size):
##    height,width = input_Image.shape
##    #print (height, width)
##
##    if width > height:
##        aspect_Ratio = (float)(width/height)
##        width = 20
##        height = round(width/aspect_Ratio)
##    else:
##        aspect_Ratio = (float)(height/width)
##        height = 20
##        width = round(height/aspect_Ratio)

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

    return cv2.resize(input_Image, (Image_Size,Image_Size), interpolation = cv2.INTER_AREA )

number = 1000000
for filename in dirnames:
    #path=os.path.join(filename)
    if filename.endswith(('.png')):
        Image_File_Path  = os.path.join(source_Image_Path,filename)

        if number%100==0:
            print (number)

        image = cv2.imread(Image_File_Path)
        
        image = cv2.bitwise_not(image)


        Dest_Image_File_Path  = destination_Image_Path + r'\\' + imageName + str(number) + '.png'  #os.path.join(destination_Image_Path,filename)
        
        cv2.imwrite(Dest_Image_File_Path,image)
        number = number + 1

        
        
        #listFileNames.append(filename)
print ('')
print (imageName)
print ('Doneeeeeee')
