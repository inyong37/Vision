# -*- coding:utf-8 -*-
# Author : Inyong Hwang
# 3. Image to pkl

import os
import pandas as pd
import cv2
import numpy as np
from tqdm import tqdm
import pickle

dir_origin = 'D:/Dataset/OCR/STR/DATA_1v4/CHARACTER'
name_chars = os.listdir(dir_origin)
name_data = []
dir_images = []
for index, name_char in tqdm(enumerate(name_chars)):
    dir_char = dir_origin + '/' + name_char
    name_images = os.listdir(dir_char)
    for name_image in name_images:
        dir_image = dir_char + '/' + name_image
        dir_images.append(dir_image)
        name_data.append((name_image, index))

name_data = pd.DataFrame(name_data, columns=['image', 'label'], index=None)

# images
images = []
for dir_image in tqdm(dir_images):
    image = cv2.imread(str(dir_image), cv2.IMREAD_GRAYSCALE)
    image = image.astype(np.float32) / 255.
    images.append(image)

# labels
labels = []
for label in name_data['label']:
    labels.append(label)

# pickles
with open('D:/dataset/OCR/STR/DATA_1v4/PKL/images.pkl', 'wb') as f:
    pickle.dump(images, f)
with open('D:/dataset/OCR/STR/DATA_1v4/PKL/labels.pkl', 'wb') as f:
    pickle.dump(labels, f)
