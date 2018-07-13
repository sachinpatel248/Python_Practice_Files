from  scipy import ndimage
import math
import numpy as np
import argparse
import cv2
from math import atan2, pi
import string
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
from keras.models import Sequential, load_model
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
from nltk.tag import pos_tag
import json
from fuzzywuzzy import fuzz

KERAS_Alphabet_model_File_Path = r'C:\Users\sachin13390\Desktop\Keras_Alphabet_Model.h5'
Alphabet_Mapping_List = list(string.ascii_uppercase)
kernel = np.ones((3,3),np.uint8)

# Load Keras Model
KERAS_Alphabet_Model = load_model(KERAS_Alphabet_model_File_Path)
