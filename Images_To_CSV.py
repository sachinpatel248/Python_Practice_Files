import numpy as np
import pandas as pd
import os
import cv2

source_Image_Folder_Path = r'C:\Users\sachin13390\Desktop\A_Z HandwrittenData'

CSV_File_Path = r'C:\Users\sachin13390\Desktop\A_Z Handwritten Data.csv'

mappingList = []
## Create your mapping list which we made earlier on sunday


root, dirs, files = os.walk(source_Image_Folder_Path).next()

numpy_Array = np.empty([1, 785], dtype = int)

dic = -1

for directory in dirs:
    print directory

    ##dic = 0
    ## According to mapping list get value of label(indes of list) using directory(sub folder name)
    ##set dic(label) value here NOTE: label would be numbers only

    root, dirsss, allfiles = os.walk(os.path.join(source_Image_Folder_Path,directory)).next()
    number = 1
    
    for filename in allfiles:
        image_Path = (os.path.join(source_Image_Folder_Path,directory,filename))

        image  =  cv2.imread(image_Path,0)

        image = image.reshape(1,784)
        

        image = np.append(dic,image)
        image = image.reshape(1,785)

        numpy_Array = np.concatenate((numpy_Array,image))

        if number%1000==0:
            print number
            print image_Path
            numpy_Array  = np.delete(numpy_Array, 0 , axis=0)
            df = pd.DataFrame(numpy_Array)
            df.to_csv(CSV_File_Path, mode='a',index=False, header=False)
            numpy_Array = np.empty([1, 785], dtype = int)
            #print (numpy_Array)
            print ('File write')

        number = number + 1

    numpy_Array  = np.delete(numpy_Array, 0 , axis=0)
    df = pd.DataFrame(numpy_Array)
    df.to_csv(CSV_File_Path, mode='a',index=False, header=False)
    numpy_Array = np.empty([1, 785], dtype = int)
    print ('FINAL File write')


