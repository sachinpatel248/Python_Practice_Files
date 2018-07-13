import cv2
import numpy as np


imagePath =r'C:\Users\sachin13390\Desktop\OC\Froms\InputImage5.jpg'
templatePath =r'C:\Users\sachin13390\Desktop\OC\Froms\InputImage3.jpg'

img = cv2.imread(imagePath)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray_image,(5,5),0)
ret3,Otsu_Threshold_GaussianBlur_Image = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
img = cv2.Canny(Otsu_Threshold_GaussianBlur_Image,100,200)

img2 = img.copy()

template = cv2.imread(templatePath)
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(template,(5,5),0)
ret3,template = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
template = cv2.Canny(template,100,200)

cv2.imwrite(r'C:\Users\sachin13390\Desktop\InputImage5.jpg',img)
cv2.imwrite(r'C:\Users\sachin13390\Desktop\InputImage3.jpg',template)

w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img,top_left, bottom_right, 255, 2)
##    cv2.imshow(meth+'image',img)
##    cv2.imshow(meth+'image',res)
    cv2.imwrite('C:\Users\sachin13390\Desktop' + '\\'+ str(meth)+'.png',res)
    
##    plt.subplot(121),plt.imshow(res,cmap = 'gray')
##    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
##    plt.subplot(122),plt.imshow(img,cmap = 'gray')
##    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
##    plt.suptitle(meth)
##    plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
