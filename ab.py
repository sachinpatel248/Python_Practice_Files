
import numpy as np
import cv2

a = np.array([[1,2,3],[2,3,4]])

newrow = [1,2,3]



z = np.zeros((1,3), dtype = np.uint8)

##a = np.append(z, a, axis=1)

A = np.concatenate((z,a))
 

imageFilePath = r'C:\Users\sachin13390\Desktop\3.png'


image = cv2.imread(imageFilePath,0)

image = cv2.bitwise_not(image)

cv2.imwrite(imageFilePath,image)
