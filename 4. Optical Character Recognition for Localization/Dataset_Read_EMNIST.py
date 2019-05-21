# -*- coding: utf-8 -*-
# Author: Inyong Hwang
# EMNIST convert png to numpy array

import os
import cv2
import pickle
from tqdm import tqdm

Dataset_Path = 'C:/Users/Inyong/Documents/PycharmProjects/STR/Dataset/EMNIST'
filenames = os.listdir(Dataset_Path)

label_ASCII = []
label_EMNIST = []

for filename in filenames:
    label_ASCII.append(filename)
    label_EMNIST.append(chr(int(filename, 16)))

X_Train_EMNIST = []
Y_Train_EMNIST = []

for _, i in tqdm(enumerate(label_ASCII)):
    Directory_Path = Dataset_Path + '/' + i
    dirnames = os.listdir(Directory_Path)
    for dirname in tqdm(dirnames):
        Images_Path = Dataset_Path + '/' + i + '/' + dirname
        if 'mit' in Images_Path:
            pass
        else:
            filenames = os.listdir(Images_Path)
            for filename in filenames:
                Image_Path = Images_Path + '/' + filename
                # print(Image_Path, chr(int(i, 16)))
                Image = cv2.imread(Image_Path, cv2.IMREAD_UNCHANGED)
                Image = cv2.resize(Image, dsize=(64, 64), interpolation=cv2.INTER_AREA)
                X_Train_EMNIST.append(Image)
                Y_Train_EMNIST.append(chr(int(i, 16)))

del Dataset_Path, filename, filenames, i, Images_Path, Image_Path, Image, _, label_ASCII, dirname, dirnames

for d in ['X_Train_EMNIST', 'Y_Train_EMNIST', 'label_EMNIST']:
    exec('with open("{}"+".pkl","wb") as f: pickle.dump({},f)'.format(d, d))

print("Done!")
