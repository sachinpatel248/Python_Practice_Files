#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# General
import os
import cv2
import argparse
import numpy as np

# Keras
from keras import backend as K
from keras import __version__
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.models import Model
from keras.layers import Dense, AveragePooling2D, GlobalAveragePooling2D, Input, Flatten, Dropout
from keras.preprocessing.image import ImageDataGenerator

import tensorflow as tf
from tensorflow.python.framework.graph_util import convert_variables_to_constants


# In[ ]:


# Folder_Path = r'C:\Users\Sachin13390\Desktop\NLP'

IM_WIDTH, IM_HEIGHT = 299, 299 #fixed size for InceptionV3

image_Dir_Not_Valid_Error = "Input image directory not valid - "


# In[ ]:


def Get_Sub_Folders_Count_From_Root_Folders(Folder_Path):
    return (len(next(os.walk(Folder_Path))[1]))


# In[ ]:


def check_If_Directory_Exists(dir_Path):
    if os.path.exists(dir_Path):
        return True

    return False


# In[ ]:


def freeze_session(session, keep_var_names=None, output_names=None, clear_devices=True):

    graph = session.graph
    with graph.as_default():
        freeze_var_names = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names = output_names or []
        output_names += [v.op.name for v in tf.global_variables()]
        input_graph_def = graph.as_graph_def()
        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""
        frozen_graph = convert_variables_to_constants(session, input_graph_def,
                                                      output_names, freeze_var_names)
        return frozen_graph


# In[ ]:


def Get_Train_And_Test_Generator(train_image_dir, test_image_dir, FLAGS):
    
    train_datagen = ImageDataGenerator(
                                        rotation_range = 20, width_shift_range=0.2, height_shift_range=0.2,
                                        rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True,
                                        vertical_flip=True, fill_mode='nearest')

    test_datagen = ImageDataGenerator(
                                        rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
                                        rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True,
                                        vertical_flip=True, fill_mode='nearest')

    
    train_generator = train_datagen.flow_from_directory(
                                                        train_image_dir,  target_size=(IM_WIDTH, IM_HEIGHT), 
                                                        batch_size=32,  class_mode='categorical')
    
    test_generator = test_datagen.flow_from_directory(
                                                        test_image_dir,  target_size=(IM_WIDTH, IM_HEIGHT), 
                                                        batch_size=32,  class_mode='categorical')

    return (train_generator, test_generator)


# In[ ]:


def Get_New_Layer_Model(base_Model, no_Of_Classes):
    
    x = base_Model.output
    x = AveragePooling2D((8, 8), border_mode='valid', name='avg_pool')(x)
    x = Dropout(0.2)(x)
    x = Flatten()(x)
    predictions = Dense(no_Of_Classes, activation='softmax')(x)
    model = Model(input=base_Model.input, output=predictions)
    
    return model


# In[ ]:


def train_Model(FLAGS):
    
    if not os.path.exists(FLAGS.train_image_dir):
        print(image_Dir_Not_Valid_Error, FLAGS.train_image_dir)
        return
    
    if not os.path.exists(FLAGS.test_image_dir):
        return (image_Dir_Not_Valid_Error, FLAGS.test_image_dir)
    
    
    
    no_Of_Classes = Get_Sub_Folders_Count_From_Root_Folders(FLAGS.train_image_dir) 
    
    
    train_generator, test_generator = Get_Train_And_Test_Generator(
                                                                    FLAGS.train_image_dir,
                                                                    FLAGS.test_image_dir,
                                                                    FLAGS)
    
    input_tensor = ''
    if(K.image_dim_ordering() == 'th'): # For tensorflow
        input_tensor = Input(shape=(3, IM_WIDTH, IM_HEIGHT))
    else:
        input_tensor = Input(shape=(IM_WIDTH, IM_HEIGHT, 3))
        
        
    # Get Inception model from Keras
    base_model = InceptionV3(input_tensor = input_tensor, weights = 'imagenet', include_top = False)
    
    for layer in base_model.layers:
        layer.trainable = False
    
    model = Get_New_Layer_Model(base_model, no_Of_Classes)
    
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    model.fit_generator(train_generator,
                        steps_per_epoch = 10,
                        epochs = FLAGS.how_many_training_steps, validation_data = test_generator, validation_steps = 16)
    
    frozen_graph = freeze_session(K.get_session(),
                                  output_names=[out.op.name for out in model.outputs])
    
    tf.train.write_graph(frozen_graph, "some_directory", "ZZZZZZZ.pb", as_text=False)
    
#     model.save(FLAGS.output_graph)


# In[ ]:


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
      '--train_image_dir',
      type=str,
      default='',
      help='Path to train folders of labeled images.'
    )
    parser.add_argument(
      '--test_image_dir',
      type=str,
      default='',
      help='Path to test folders of labeled images.'
    )
    parser.add_argument(
      '--output_graph',
      type=str,
      default='/tmp/output_graph.pb',
      help='Where to save the trained graph.'
    )
    parser.add_argument(
      '--output_labels',
      type=str,
      default='/tmp/output_labels.txt',
      help='Where to save the trained graph\'s labels.'
    )
    parser.add_argument(
      '--summaries_dir',
      type=str,
      default='/tmp/retrain_logs',
      help='Where to save summary logs for TensorBoard.'
    )
    parser.add_argument(
      '--how_many_training_steps',
      type=int,
      default=4000,
      help='How many training steps to run before ending.'
    )
    parser.add_argument(
      '--learning_rate',
      type=float,
      default=0.01,
      help='How large a learning rate to use when training.'
    )
    parser.add_argument(
      '--testing_percentage',
      type=int,
      default=10,
      help='What percentage of images to use as a test set.'
    )
    parser.add_argument(
      '--validation_percentage',
      type=int,
      default=10,
      help='What percentage of images to use as a validation set.'
    )
    parser.add_argument(
      '--eval_step_interval',
      type=int,
      default=10,
      help='How often to evaluate the training results.'
    )
    parser.add_argument(
      '--train_batch_size',
      type=int,
      default=100,
      help='How many images to train on at a time.'
    )
    parser.add_argument(
      '--test_batch_size',
      type=int,
      default=-1,
      help="""\
      How many images to test on. This test set is only used once, to evaluate
      the final accuracy of the model after training completes.
      A value of -1 causes the entire test set to be used, which leads to more
      stable results across runs.\
      """
    )
    parser.add_argument(
      '--validation_batch_size',
      type=int,
      default=100,
      help="""\
      How many images to use in an evaluation batch. This validation set is
      used much more often than the test set, and is an early indicator of how
      accurate the model is during training.
      A value of -1 causes the entire validation set to be used, which leads to
      more stable results across training iterations, but may be slower on large
      training sets.\
      """
    )
    parser.add_argument(
      '--print_misclassified_test_images',
      default=False,
      help="""\
      Whether to print out a list of all misclassified test images.\
      """,
      action='store_true'
    )
    parser.add_argument(
      '--model_dir',
      type=str,
      default='/tmp/imagenet',
      help="""\
      Path to classify_image_graph_def.pb,
      imagenet_synset_to_human_label_map.txt, and
      imagenet_2012_challenge_label_map_proto.pbtxt.\
      """
    )
    parser.add_argument(
      '--bottleneck_dir',
      type=str,
      default='/tmp/bottleneck',
      help='Path to cache bottleneck layer values as files.'
    )
    parser.add_argument(
      '--final_tensor_name',
      type=str,
      default='final_result',
      help="""\
      The name of the output classification layer in the retrained graph.\
      """
    )
    parser.add_argument(
      '--flip_left_right',
      default=False,
      help="""\
      Whether to randomly flip half of the training images horizontally.\
      """,
      action='store_true'
    )
    parser.add_argument(
      '--random_crop',
      type=int,
      default=0,
      help="""\
      A percentage determining how much of a margin to randomly crop off the
      training images.\
      """
    )
    parser.add_argument(
      '--random_scale',
      type=int,
      default=0,
      help="""\
      A percentage determining how much to randomly scale up the size of the
      training images by.\
      """
    )
    parser.add_argument(
      '--random_brightness',
      type=int,
      default=0,
      help="""\
      A percentage determining how much to randomly multiply the training image
      input pixels up or down by.\
      """
    )
    
    FLAGS, unparsed = parser.parse_known_args()
    
    train_Model(FLAGS)
    
    


# # ###################### Testing ######################

# In[ ]:


# model_File_Path = r'C:\Users\Sachin13390\Desktop\Transfer_learning\Trained_Model\5_Epoch_Trained_Model.pb'
# image_Folder_Path = r'C:\Users\Sachin13390\Desktop\Transfer_learning\Test_Images'
# image_Path = r'C:\Users\Sachin13390\Desktop\Transfer_learning\Test_Images\7.jpg'

# model = load_model(model_File_Path)


# In[ ]:


# for i in range (1,14):
#     image_Path = os.path.join(image_Folder_Path, (str(i) + '.jpg'))
# #     print(image_Path)
#     image = cv2.imread(image_Path)
#     image = cv2.resize(image, (299, 299))
# #     cv2.imshow('image',image)
# #     cv2.waitKey(0)
#     image = image.reshape(1, 299, 299, 3)
#     image = image/255

#     print(np.;\argmax(model.predict(image)))


# In[ ]:


# python transfer_Learning.py --train_image_dir=C:\\Users\\Sachin13390\\Desktop\\Transfer_learning\\Data_CNN\\Train  --test_image_dir=C:\\Users\\Sachin13390\\Desktop\\Transfer_learning\\Data_CNN\\Test  --output_graph=C:\\Users\\Sachin13390\\Desktop\\Transfer_learning\\Trained_Model\\trained_Model.h5  --how_many_training_steps=1


# In[ ]:




