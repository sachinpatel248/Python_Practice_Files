from mnist import MNIST
import cv2
from numpy import array
from PIL import Image
import numpy as np
import pandas as pd


#mndata = MNIST(r'C:\Users\sachin13390\Desktop\Samples')

CSV_FILE_PATH = r'C:\Users\sachin13390\Desktop\emnist-letters-train.csv'

#images, labels = mndata.load_training()

image_Path = r'C:\Users\sachin13390\Desktop\A-Z Data'
count = 1

df = pd.read_csv(CSV_FILE_PATH)

Labels = df.iloc[:,0]

Images = df.drop(df.columns[0],axis = 1)

print (type(Images))


index = 0

rows = 28
cols = 28

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)

for label in Labels:
    new_image_Path = image_Path + '\\' + str(label)+ '\\' + str(label) + '_' + str(index+1) + '.png'
    #print (new_image_Path)
    image = Images.loc[index].values.astype('uint8')
    image = np.resize(image, (28,28,1))
    image=cv2.flip(image,1)
    image = cv2.warpAffine(image,M,(cols,rows))
    cv2.imwrite(new_image_Path,image)
    

    index = index + 1

    if index%100==0:
        print (index)
    

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

    

