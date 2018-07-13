import cv2
import numpy as np

imageFilePath = r'C:\Users\sachin13390\Desktop\OC\Froms\InputImage5.jpg'
kernel = np.ones((5,5),np.uint8)

file_Path = r'C:\Users\sachin13390\Desktop\Temp Images'

image = cv2.imread(imageFilePath)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


for i in range(25,255):
    ret,th1 = cv2.threshold(gray_image,i,255,cv2.THRESH_BINARY)
    cv2.imwrite(file_Path + '\\' + str(i) + '.jpg',th1)
