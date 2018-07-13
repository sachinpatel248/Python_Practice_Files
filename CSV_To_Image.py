import csv
from PIL import Image
import numpy as np
import string
import os

print ("Runs using Python 3.x")

csv_File_Path = r'C:\Users\Sachin13390\Desktop\Kaggle-Emnist\AAA.csv'

count = 1
last_digit_Name =  None

image_Folder_Path = r'C:\Users\Sachin13390\Desktop\New Images'
Alphabet_Mapping_List = range(0, 10)

for alphabet in Alphabet_Mapping_List:
    path = image_Folder_Path + '\\' + str(alphabet)
    if not os.path.exists(path):
        os.makedirs(path)


with open(csv_File_Path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    for row in reader:
        digit_Name = row.pop(0)
        image_array = np.asarray(row)
        image_array = image_array.reshape(28, 28)
        new_image = Image.fromarray(image_array.astype('uint8'))

        if last_digit_Name != str(Alphabet_Mapping_List[(int)(digit_Name)]):
            last_digit_Name = str(Alphabet_Mapping_List[(int)(digit_Name)])
            count = 0
            
        
        image_Path = image_Folder_Path + '\\' + str(digit_Name) + '\\' + str(count) + '.png'
        new_image.save(image_Path)
        count = count + 1

        if count % 1000 ==0:
            print ("Images processed: " + str(count))
            




