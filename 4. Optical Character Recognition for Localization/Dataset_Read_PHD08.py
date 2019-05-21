# -*- coding: utf-8 -*-
# Author: Inyong Hwang
# PHD08 convert png to numpy array

import os
import cv2
import numpy as np
import pickle
from tqdm import tqdm

Dataset_Path = 'C:/Users/Inyong/Documents/PycharmProjects/STR/Dataset/PHD08'
filenames = os.listdir(Dataset_Path)

label_PHD08 = []

for filename in filenames:
    label_PHD08.append(filename)

X_Train_PHD08 = []
Y_Train_PHD08 = []

for _, i in tqdm(enumerate(label_PHD08)):
    Images_Path = Dataset_Path + '/' + i
    filenames = os.listdir(Images_Path)
    for filename in tqdm(filenames):
        Image_Path = Images_Path + '/' + filename
        # print(Images_Path, i)
        stream = open(Image_Path.encode("utf-8"), "rb")
        byte = bytearray(stream.read())
        array = np.asarray(byte, dtype=np.uint8)
        Image = cv2.imdecode(array, cv2.IMREAD_GRAYSCALE)
        Image = cv2.resize(Image, dsize=(64, 64), interpolation=cv2.INTER_LINEAR)
        X_Train_PHD08.append(Image)
        Y_Train_PHD08.append(i)

del Dataset_Path, filename, filenames, i, Images_Path, Image_Path, Image, _

for d in ['X_Train_PHD08', 'Y_Train_PHD08', 'label_PHD08']:
    exec('with open("{}"+".pkl","wb") as f: pickle.dump({},f)'.format(d, d))

print("Done!")
