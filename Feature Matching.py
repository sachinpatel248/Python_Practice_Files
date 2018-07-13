import numpy as np
import cv2
##
##print(cv2.__version__ )
##
##help(cv2)


imagePath =r'C:\Users\sachin13390\Desktop\OC\Froms\InputImage5.jpg'
templatePath =r'C:\Users\sachin13390\Desktop\OC\Froms\InputImage3.jpg'

img1 = cv2.imread(imagePath,cv2.COLOR_BGR2GRAY)         # queryImage
blur = cv2.GaussianBlur(img1,(5,5),0)
ret3,img1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
##img1 = cv2.Canny(img1,100,200)

img2 = cv2.imread(templatePath, cv2.COLOR_BGR2GRAY) # trainImage
blur = cv2.GaussianBlur(img2,(5,5),0)
ret3,img1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
##img2 = cv2.Canny(img2,100,200)

sift = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\temp1234.jpg',img3)

#cv2.imshow('img3',img3)
