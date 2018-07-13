import cv2
import os
from PIL import Image


source_Image_Path = r'C:\Users\Sachin\Desktop\DATA\Latin\C'

destination_Image_Path = r'C:\Users\Sachin\Desktop\Deep Data\Latin\C'


dirnames = os.listdir(source_Image_Path)

imageName = 'C'

listFileNames = []
number = 1

def RGBA_TO_RGB_Image(image):
    width = 278
    height = 278
    for y in range(height):
        for x in range(width):
            a=image[x, y]
            if not ( a[0]==a[1]==a[2]==0 and a[3]==255):
                a[0]=a[1]=a[2]=a[3]=255
                image[x, y] = a
    return image;

for filename in dirnames:
    #path=os.path.join(filename)
    if filename.endswith(('.png')):
        Image_File_Path  = os.path.join(source_Image_Path,filename)
        print (number)

        image = cv2.imread(Image_File_Path,-1)
        image=RGBA_TO_RGB_Image(image)
        
        #cv2.imwrite(r'C:\Users\Sachin\Desktop\aaa.jpg',image)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        image = cv2.bitwise_not(image)
        #cv2.imshow( "image", image );
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        im2,contours,hierarchy = cv2.findContours(image,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        

        x,y,w,h = cv2.boundingRect(contours[0])
        cropped_im =image[y:y+h, x:x+w]
        #cv2.imshow( "cropped_im", cropped_im );
        resize_image = cv2.resize(cropped_im, (28, 28), interpolation = cv2.INTER_AREA)
        #cv2.imshow( "resize_image", resize_image );

        Dest_Image_File_Path  = destination_Image_Path + r'\\' + imageName + str(number) + '.png'  #os.path.join(destination_Image_Path,filename)
        
        cv2.imwrite(Dest_Image_File_Path,resize_image)
        number = number + 1

        
        
        #listFileNames.append(filename)
