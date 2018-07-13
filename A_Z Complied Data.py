import cv2
import os
import numpy as np


source_Image_Path = r'C:\Users\sachin13390\Desktop\A-Z Raw Data\S'

destination_Image_Path = r'C:\Users\sachin13390\Desktop\A_Z Complied Data\S'


dirnames = os.listdir(source_Image_Path)

imageName = 'S'
print ('')
print (imageName)
print ('')


number = 1

def RGBA_TO_RGB_Image(image):
    width = 128
    height = 128
    for y in range(height):
        for x in range(width):
            a=image[x, y]
            if not ( a[0]==a[1]==a[2]==0 and a[3]==255):
                a[0]=a[1]=a[2]=a[3]=255
                image[x, y] = a
    return image;

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

number = 1
for filename in dirnames:
    #path=os.path.join(filename)
    if filename.endswith(('.png')):
        Image_File_Path  = os.path.join(source_Image_Path,filename)

        if number%100==0:
            print (number)

        image = cv2.imread(Image_File_Path,-1)
        
        image = cv2.bitwise_not(image)
        #cv2.imshow( "image", image );
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        im2,contours,hierarchy = cv2.findContours(image,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        Biggest_Countour = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(Biggest_Countour)
        cropped_im =image[y:y+h, x:x+w]
        #cv2.imshow( "cropped_im", cropped_im );
        resize_image = getNewResizedImage(cropped_im,28)
        #cv2.imshow( "resize_image", resize_image );

        Dest_Image_File_Path  = destination_Image_Path + r'\\' + imageName + str(number) + '.png'  #os.path.join(destination_Image_Path,filename)
        
        cv2.imwrite(Dest_Image_File_Path,resize_image)
        number = number + 1

        
        
        #listFileNames.append(filename)
print ('')
print (imageName)
print ('Doneeeeeee')
