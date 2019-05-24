# -*- coding: utf-8 -*-
# Author: Inyong Hwang
# Divide Train and Test set

import os
import pickle
from sklearn.model_selection import train_test_split
from tqdm import tqdm

Datasets_Path = 'C:/Users/Inyong/Documents/PycharmProjects/STR/Dataset/PKL'
Datasets = os.listdir(Datasets_Path)

Label = []
X = []
Y = []

for Dataset in Datasets:
    Dataset_Path = Datasets_Path + '/' +Dataset
    with open(Dataset_Path, 'rb') as f:
        Data = pickle.load(f)
        if 'label' in Dataset:
            Label.extend(Data)
        elif 'X' in Dataset:
            X.extend(Data)
        else:
            Y.extend(Data)
        f.close()

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.2, random_state=37, shuffle=True)

with open('C:/Users/Inyong/Documents/PycharmProjects/STR/Dataset/DIVIDED/X_Test.pkl', 'wb') as f:
    pickle.dump(X_Test, f)
    f.close()

with open('C:/Users/Inyong/Documents/PycharmProjects/STR/Dataset/DIVIDED/Y_Test.pkl', 'wb') as f:
    pickle.dump(Y_Test, f)
    f.close()

length = int(len(X_Train)/10)
each = []
each.append(0)
for i in range(1, 11):
    each.append(length*i)

for i in tqdm(range(0, 10)):
    with open('C:/Users/Inyong/Documents/PycharmProjects/STR/Dataset/DIVIDED/X_Train_' + str(i) + '.pkl', 'wb') as f:
        if i == 10:
            pickle.dump(X_Train[each[i]:], f)
        else:
            pickle.dump(X_Train[each[i]:each[i+1]], f)
        f.close()
    with open('C:/Users/Inyong/Documents/PycharmProjects/STR/Dataset/DIVIDED/Y_Train_' + str(i) + '.pkl', 'wb') as f:
        if i == 10:
            pickle.dump(Y_Train[each[i]:], f)
        else:
            pickle.dump(Y_Train[each[i]:each[i+1]], f)
        f.close()
