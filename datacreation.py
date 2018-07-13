from mnist import MNIST
import cv2
from numpy import array
from PIL import Image
import numpy as np


mndata = MNIST(r'C:\Users\sachin13390\Desktop\Samples')

#images, labels = mndata.load_training()

image_Path = r'C:\Users\sachin13390\Desktop\NEWDATA'
count = 1

##for index,image in enumerate(images):
##    new_image_Path = image_Path + '\\' + str(labels[index])+ '\\' + str(labels[index]) + '_' + str(index+1) + '.png'
##    #print (new_image_Path)
##    img = array(images[index])
##    img = np.resize(img,(28,28,1))
##    cv2.imwrite(new_image_Path,img)
##
##    if (index%100)==0:
##        print(index)
##        



# or
images, labels = mndata.load_testing()

count = 0
for imagecount in images:
    count = count + 1

print(count)
    

