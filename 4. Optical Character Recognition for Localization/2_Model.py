# -*- coding:utf-8 -*-
# Author : Inyong Hwang
#

import numpy as np
import pickle
from keras.models import Model
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.optimizers import Adam

origin_dir = 'D:/dataset/KAGGLE/XRAY/PKL/'

with open(origin_dir + 'train_image.pkl', 'rb') as f:
    train_image = pickle.load(f)
with open(origin_dir + 'train_label.pkl', 'rb') as f:
    train_label = pickle.load(f)
with open(origin_dir + 'val_image.pkl', 'rb') as f:
    val_image = pickle.load(f)
with open(origin_dir + 'val_label.pkl', 'rb') as f:
    val_label = pickle.load(f)
with open(origin_dir + 'test_image.pkl', 'rb') as f:
    test_image = pickle.load(f)
with open(origin_dir + 'test_label.pkl', 'rb') as f:
    test_label = pickle.load(f)


def test_model():
    i = Input(shape=(224, 224, 3), name='Input_Image')
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='Conv1_1')(i)
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='Conv1_2')(x)
    x = MaxPooling2D((2, 2), name='pool1')(x)
    x = Flatten(name='flatten')(x)
    x = Dense(1024, activation='relu', name='fc1')(x)
    x = Dropout(0.7, name='dropout1')(x)
    x = Dense(512, activation='relu', name='fc2')(x)
    x = Dropout(0.5, name='dropout2')(x)
    y = Dense(2, activation='softmax', name='fc3')(x)
    model = Model(inputs=i, outputs=y)
    return model


model = test_model()
model.summary()
model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer=Adam(lr=0.0001, decay=1e-5))

train_image = np.array(train_image)
train_label = np.array(train_label)
test_image = np.array(test_image)
test_label = np.array(test_label)

model.fit(x=train_image, y=train_label, epochs=100, batch_size=1, validation_data=(test_image, test_label), verbose=2)

val_image = np.array(val_image)
val_label = np.array(val_label)

model.evaluate(x=val_image, y=val_label)