import numpy as np
import argparse
import cv2
 
imagePath =r'C:\Users\sachin13390\Desktop\OC\Froms\InputImage5.jpg'

image = cv2.imread(imagePath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
ret3,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#thresh = cv2.bitwise_not(thresh)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\thresh.jpg',thresh)

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),1)



cv2.imwrite(r'C:\Users\sachin13390\Desktop\countours.jpg',image)
