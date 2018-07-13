import cv2
import os
import numpy as np


imageName = 'A'

source_Image_Path = r'C:\Users\sachin13390\Desktop\A_Z HandwrittenData\\' + imageName

destination_Image_Path = r'C:\Users\sachin13390\Desktop\A'



root, dirs, files = os.walk(source_Image_Path).next()


print ('')
print (imageName)
print ('')


def getNewResizedImage(input_Image, Image_Size):

    height,width = input_Image.shape
    #print (height, width)

    if width > height:
        aspect_Ratio = (float)(width/height)
        width = 20
        height = int(round(width/aspect_Ratio))
    else:
        aspect_Ratio = (float)(height/width)
        height = 20
        width = int(round(height/aspect_Ratio))
		
    input_Image = cv2.resize(input_Image, (width,height), interpolation = cv2.INTER_AREA )
    
    height,width = input_Image.shape
    

    number_Of_Column_To_Add = Image_Size-width
    temp_Column = np.zeros( (height , int(number_Of_Column_To_Add/2)), dtype = np.uint8)
    input_Image = np.append(temp_Column, input_Image, axis=1)
    input_Image = np.append(input_Image, temp_Column, axis=1)

    height,width = input_Image.shape


    number_Of_Row_To_Add = Image_Size-height
    temp_Row= np.zeros( (int(number_Of_Row_To_Add/2) , width ), dtype = np.uint8)
    input_Image = np.concatenate((temp_Row,input_Image))
    input_Image = np.concatenate((input_Image,temp_Row))

    return cv2.resize(input_Image, (Image_Size,Image_Size), interpolation = cv2.INTER_AREA )

number = 1
for filename in files:
    #path=os.path.join(filename)
    if filename.endswith(('.png')):
        Image_File_Path  = os.path.join(source_Image_Path,filename)

        if number%1000==0:
            print (number)

        image = cv2.imread(Image_File_Path,0)

        im2,contours,hierarchy = cv2.findContours(image,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
               
        Biggest_Countour = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(Biggest_Countour)
        image = cv2.imread(Image_File_Path,0)
        
        resize_image =image[y:y+h, x:x+w]

        resize_image = getNewResizedImage(resize_image,28)

        Dest_Image_File_Path  = destination_Image_Path + '\\' + imageName+ '_' + str(number) + '.png'  #os.path.join(destination_Image_Path,filename)
        cv2.imwrite(Dest_Image_File_Path,resize_image)
        number = number + 1

        
        
        #listFileNames.append(filename)
print ('')
print (imageName)
print ('Doneeeeeee')
