import numpy as np
import argparse
import cv2
 
imagePath =r'C:\Users\sachin13390\Desktop\OC\Froms\
.jpg'

image = cv2.imread(imagePath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
##gray = cv2.bitwise_not(gray)
##cv2.imwrite(r'C:\Users\sachin13390\Desktop\gray.jpg',gray)
##
##thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
##cv2.imwrite(r'C:\Users\sachin13390\Desktop\thresh.jpg',gray)


blur = cv2.GaussianBlur(gray,(5,5),0)
ret3,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#thresh = cv2.bitwise_not(thresh)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\thresh.jpg',thresh)

coords = np.column_stack(np.where(thresh > 0))
angle = cv2.minAreaRect(coords)[-1]
 
if angle < -45:
    angle = -(90 + angle)
 
else:
    angle = -angle
#angle = -4 
# rotate the image to deskew it
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# draw the correction angle on the image so we can validate it
#cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

cv2.imwrite(r'C:\Users\sachin13390\Desktop\rotated.jpg',rotated)
 
# show the output image
print("[INFO] angle: {:.3f}".format(angle))
cv2.imshow("Input", image)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)


















	
