import os
 

path = r'C:\Users\sachin13390\Desktop\Datasets\Nmist\notMNIST_large\I'


root, dirs, files = os.walk(path).next()

fileExtension = '.png'

number = 1
for filename in files:
    #print os.path.join(root,filename)
    os.rename(os.path.join(root,filename),os.path.join(root,'I'+'_' + str(number) + fileExtension))
    number = number + 1

    if number % 100==0:
        print number

##for directory in dirs:
##    print directory
##
##    root, dirsss, allfiles = os.walk(os.path.join(path,directory)).next()
##    number = 1
##    
##    for filename in allfiles:
##        #print os.path.join(root,filename)
##        os.rename(os.path.join(root,filename),os.path.join(root,str(directory)+'_' + str(number) + fileExtension))
##
##
##        number = number + 1
##        if number % 100==0:
##            print number

        

##for filename in os.listdir(path):
##    filename_without_ext = os.path.splitext(filename)[0]
##    extension = os.path.splitext(filename)[1]
##    new_file_name = filename_without_ext+"_n"
##    new_file_name_with_ext = new_file_name+extension
##    print(new_file_name_with_ext)
##    os.rename(os.path.join(path,filename),os.path.join(path,new_file_name_with_ext))
