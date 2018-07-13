import cv2
import numpy as np

imageFilePath = r'C:\Users\sachin13390\Desktop\OC\InputImage1.jpg'
kernel = np.ones((5,5),np.uint8)



image = cv2.imread(imageFilePath)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edege = cv2.Canny(gray_image,100,200,apertureSize = 3)

Gaussian_threshold_image = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)

ret2,Otsu_Threshold_Image = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(gray_image,(5,5),0)
ret3,Otsu_Threshold_GaussianBlur_Image = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

Adaptive_Mean_Threshold_Image = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)

cv2.imshow('1 Original Image',image)
cv2.imshow('2 Gray',gray_image)
cv2.imshow('3 GAUSSIAN Threshold',Gaussian_threshold_image)
cv2.imshow('4 Otsu Threshold',Gaussian_threshold_image)




final = cv2.medianBlur(Gaussian_threshold_image, 3)
cv2.imshow('4 Filteredd GAUSSIAN Threshold',final)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\temp1234.jpg',final)


cv2.imshow('5 Otsu Blur Threshold',Otsu_Threshold_GaussianBlur_Image)

ret,thresh1 = cv2.threshold(gray_image,135,255,cv2.THRESH_BINARY)
#cv2.imshow('6 edege',edege)


##opening = cv2.morphologyEx(Gaussian_threshold_image, cv2.MORPH_OPEN, kernel)
##cv2.imshow('3 Open GAUSSIAN Threshold',opening)
##
##opening = cv2.morphologyEx(Gaussian_threshold_image, cv2.MORPH_OPEN, kernel)
##cv2.imshow('4 Open Otsu Threshold',opening)
##
##opening = cv2.morphologyEx(Otsu_Threshold_GaussianBlur_Image, cv2.MORPH_OPEN, kernel)
##cv2.imshow('5 Open Otsu Blur Threshold',opening)
##
##opening = cv2.morphologyEx(Adaptive_Mean_Threshold_Image, cv2.MORPH_OPEN, kernel)
##cv2.imshow('6 Open Adaptive Mean Threshold',opening)


cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()  
print ("done")
