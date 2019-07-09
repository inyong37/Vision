# -*- coding:utf-8 -*-
# Author: Inyong Hwang
# ResNet for STR
# Prediction Test

import sys
module_dir = 'C:/Users/terry/Desktop/Project/Vision/4. Optical Character Recognition for Localization/STR/1_DATA_CODE_v4/'
sys.path.append(module_dir)
import dict
import os
import cv2
import numpy as np
from keras.models import model_from_json

input_dir = 'D:/Dataset/OCR/STD/AIHUB/TEST/'
image_dirs = []
images = []
image_names = os.listdir(input_dir)
for image_name in image_names:
    # print(image_name)
    image_dirs.append(input_dir + image_name)

for image_dir in image_dirs:
    stream = open(image_dir.encode('utf-8'), 'rb')
    byte = bytearray(stream.read())
    array = np.array(byte, dtype=np.uint8)
    image = cv2.imdecode(array, cv2.IMREAD_GRAYSCALE)
    images.append(image)

# images = np.array(images)
images_15 = []
images_20 = []
images_64 = []
for image in images:
    image_15 = cv2.resize(image, (15, 15), interpolation=cv2.INTER_LANCZOS4)
    image_20 = cv2.resize(image, (20, 20), interpolation=cv2.INTER_LANCZOS4)
    image_64 = cv2.resize(image, (64, 64), interpolation=cv2.INTER_LANCZOS4)
    images_15.append(image_15)
    images_20.append(image_20)
    images_64.append(image_64)

images_15 = np.array(images_15)
images_15 = images_15[:, :, :, np.newaxis]
images_20 = np.array(images_20)
images_20 = images_20[:, :, :, np.newaxis]
images_64 = np.array(images_64)
images_64 = images_64[:, :, :, np.newaxis]

model_dir_15 = 'D:/Dataset/OCR/STR/COLAB_OUTPUT_6/resnet56v2_101_200_15/model.json'
model_dir_20 = 'D:/Dataset/OCR/STR/COLAB_OUTPUT_6/resnet56v2_101_200_20/model.json'
model_dir_64 = 'D:/Dataset/OCR/STR/COLAB_OUTPUT_5/resnet56v2_151_200/model.json'
weights_dir_15 = 'D:/Dataset/OCR/STR/COLAB_OUTPUT_6/resnet56v2_101_200_15/weights.h5'
weights_dir_20 = 'D:/Dataset/OCR/STR/COLAB_OUTPUT_6/resnet56v2_101_200_20/weights.h5'
weights_dir_64 = 'D:/Dataset/OCR/STR/COLAB_OUTPUT_5/resnet56v2_151_200/weights.h5'

json_file_15 = open(model_dir_15, 'r')
json_model_15 = json_file_15.read()
json_file_15.close()
model_15 = model_from_json(json_model_15)
model_15.load_weights(weights_dir_15)

pres = model_15.predict(images_15)
pre_15 = []
for pre in pres:
    value = np.argmax(pre)
    pre_15.append(value)

json_file_20 = open(model_dir_20, 'r')
json_model_20 = json_file_20.read()
json_file_20.close()
model_20 = model_from_json(json_model_20)
model_20.load_weights(weights_dir_20)

pres = model_20.predict(images_20)
pre_20 = []
for pre in pres:
    value = np.argmax(pre)
    pre_20.append(value)

json_file_64 = open(model_dir_64, 'r')
json_model_64 = json_file_64.read()
json_file_64.close()
model_64 = model_from_json(json_model_64)
model_64.load_weights(weights_dir_64)

pres = model_64.predict(images_64)
pre_64 = []
for pre in pres:
    value = np.argmax(pre)
    pre_64.append(value)


def find_word(predictions, dictionary):
    for prediction in predictions:
        for key, value in dictionary.items():
            if value == prediction:
                print('prediction:', key)
    return None


new = dict.character_encoding()
find_word(predictions=pre_15, dictionary=new)
find_word(predictions=pre_20, dictionary=new)
find_word(predictions=pre_64, dictionary=new)
