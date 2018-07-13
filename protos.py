import os


rootDir = r'F:\models-master\research\object_detection\protos'


for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
        if fname.endswith('.proto'):
            print('F:\\bin\protoc object_detection/protos/' +str(fname)+' --python_out=.')
        
