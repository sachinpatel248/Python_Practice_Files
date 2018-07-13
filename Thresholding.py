import cv2
import numpy as np

imageFilePath =r'C:\Users\sachin13390\Desktop\OC\Froms\InputImage5.jpg'
kernel = np.ones((3,3),np.uint8)



image = cv2.imread(imageFilePath)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edege = cv2.Canny(gray_image,100,200,apertureSize = 3)

Gaussian_threshold_image = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)

ret2,Otsu_Threshold_Image = cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(gray_image,(5,5),0)
ret3,Otsu_Threshold_GaussianBlur_Image = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\Otsu_Threshold_GaussianBlur_Image.jpg',Otsu_Threshold_GaussianBlur_Image)

kernel = np.ones((5,5), np.uint8)
Otsu_Threshold_GaussianBlur_Image = cv2.bitwise_not(Otsu_Threshold_GaussianBlur_Image)

img_erosion = cv2.erode(Otsu_Threshold_GaussianBlur_Image, kernel, iterations=1)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\img_erosion.jpg',img_erosion)

img_dilation = cv2.dilate(Otsu_Threshold_GaussianBlur_Image, kernel, iterations=5)

cv2.imwrite(r'C:\Users\sachin13390\Desktop\img_dilation.jpg',img_dilation)

Adaptive_Mean_Threshold_Image = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)


opening = cv2.morphologyEx(Otsu_Threshold_GaussianBlur_Image, cv2.MORPH_OPEN, kernel)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\opening.jpg',opening)

closing = cv2.morphologyEx(Otsu_Threshold_GaussianBlur_Image, cv2.MORPH_CLOSE, kernel)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\closing.jpg',closing)
