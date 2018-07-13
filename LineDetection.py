import numpy as np
import argparse
import cv2
from math import atan2, pi

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

imagePath =r'C:\Users\sachin13390\Desktop\OC\Froms\InputImage6.jpg'




image = cv2.imread(imagePath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

##blur = cv2.GaussianBlur(gray,(3,3),0)
##ret3,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
##cv2.imwrite(r'C:\Users\sachin13390\Desktop\thresh.jpg',thresh)


edges = cv2.Canny(gray,100,200)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\edges.jpg',edges)

print("start")

def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 25, minLineLength=100, maxLineGap=5)

for line in lines:
    #print ((line.shape))
    #x1,y1,x2,y2=tuple(totuple(i) for i in line)
    x1=line[0][0];
    #print ((line.shape))
    y1=line[0][1];
    x2=line[0][2];
    y2=line[0][3];

    deltax = x2 - x1
    deltay = y2 - y1
    angle_rad = atan2(deltay,deltax)
    angle = angle_rad*180.0/pi
    #cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
##    print("333333")

(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
print("2222")
rotated = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

cv2.imwrite(r'C:\Users\sachin13390\Desktop\rotated.jpg',rotated)

#thresh = cv2.bitwise_not(thresh)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\lines.jpg',image)

















	
