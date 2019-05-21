# Reference Code: https://keras.io/examples/cifar10_resnet/
# Modified by Inyong Hwang
# Character level STR with ResNet Version 2

import keras
from keras.layers import Dense, Conv2D, BatchNormalization, Activation
from keras.layers import AveragePooling2D, Input, Flatten
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, LearningRateScheduler
from keras.callbacks import ReduceLROnPlateau
from keras.regularizers import l2
from keras.models import Model
import numpy as np
import os
import pickle
from sklearn.model_selection import train_test_split

# Load Dataset
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

X = np.array(X)
X = X[:, :, :, np.newaxis]

Y = np.array(Y)

t = keras.preprocessing.text.Tokenizer(lower=False)
t.fit_on_texts(Y)
Y = t.texts_to_sequences(Y)
Classes = len(t.word_index)
Y = keras.utils.to_categorical(Y, Classes+1)

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.2, random_state=37, shuffle=True)
X_Train = X_Train.astype('float32') / 255
X_Test = X_Test.astype('float32') / 255
X_Train_Mean = np.mean(X_Train, axis=0)
X_Train -= X_Train_Mean
X_Test -= X_Train_Mean

del X, Y, Dataset_Path, Datasets_Path, Datasets, Dataset, Data, f, Label

print('x_train shape:', X_Train.shape)
print(X_Train.shape[0], 'train samples')
print(X_Test.shape[0], 'test samples')
print('y_train shape:', Y_Train.shape)

# Define Model
version = 2
n = 6
depth = n * 9 + 2
input_shape = X_Train.shape[1:]
batch_size = 128
epochs = 200
model_type = 'ResNet%dv%d' % (depth, version)


def lr_schedule(epoch):
    lr = 1e-3
    if epoch > 180:
        lr *= 0.5e-3
    elif epoch > 160:
        lr *= 1e-3
    elif epoch > 120:
        lr *= 1e-2
    elif epoch > 80:
        lr *= 1e-1
    print('Learning rate: ', lr)
    return lr


def resnet_layer(inputs,
                 filters=16,
                 kernel_size=3,
                 strides=1,
                 activation='relu',
                 batch_normalization=True,
                 conv_first=True):
    conv = Conv2D(filters=filters,
                  kernel_size=kernel_size,
                  strides=strides,
                  padding='same',
                  kernel_initializer='he_normal',
                  kernel_regularizer=l2(1e-4))
    x = inputs
    if conv_first:
        x = conv(x)
        if batch_normalization:
            x = BatchNormalization()(x)
        if activation is not None:
            x = Activation(activation)(x)
    else:
        if batch_normalization:
            x = BatchNormalization()(x)
        if activation is not None:
            x = Activation(activation)(x)
        x = conv(x)
    return x


def resnet_v2(input_shape=input_shape,
              depth=depth,
              classes=Classes):
    filters_in = 16
    resnet_blocks = int((depth - 2) / 9)
    inputs = Input(shape=input_shape)
    x = resnet_layer(inputs=inputs, filters=filters_in, conv_first=True)
    for stage in range(3):
        for resnet_block in range(resnet_blocks):
            activation = 'relu'
            batch_normalization = True
            strides = 1
            if stage == 0:
                filters_out = filters_in * 4
                if resnet_block == 0:
                    activation = None
                    batch_normalization = False
            else:
                filters_out = filters_in * 2
                if resnet_block == 0:
                    strides = 2
            y = resnet_layer(inputs=x, filters=filters_in, kernel_size=1, strides=strides, activation=activation, batch_normalization=batch_normalization, conv_first=False)
            y = resnet_layer(inputs=y, filters=filters_in, conv_first=False)
            y = resnet_layer(inputs=y, filters=filters_out, kernel_size=1, conv_first=False)
            if resnet_block == 0:
                x = resnet_layer(inputs=x, filters=filters_out, kernel_size=1, strides=strides, activation=None, batch_normalization=False)
            x = keras.layers.add([x, y])
        filters_in = filters_out

    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = AveragePooling2D(pool_size=8)(x)
    y = Flatten()(x)
    outputs = Dense(classes+1, activation='softmax', kernel_initializer='he_normal')(y)
    model = Model(inputs=inputs, outputs=outputs)
    return model


model = resnet_v2(input_shape=input_shape, depth=depth)
model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=lr_schedule(0)), metrics=['accuracy'])
model.summary()
print(model_type)

# Save
save_dir = os.path.join(os.getcwd(), 'saved_models')
model_name = 'STR_%s_model.{epoch:03d}.hg' % model_type
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)
filepath = os.path.join(save_dir, model_name)
checkpoint = ModelCheckpoint(filepath=filepath,
                             monitor='val_acc',
                             verbose=1,
                             save_best_only=True)

lr_scheduler = LearningRateScheduler(lr_schedule)

lr_reducer = ReduceLROnPlateau(factor=np.sqrt(0.1),
                               cooldown=0,
                               patience=5,
                               min_lr=0.5e-6)

callbacks = [checkpoint, lr_reducer, lr_scheduler]

model.fit(X_Train, Y_Train, batch_size=batch_size, epochs=epochs, verbose=1, callbacks=callbacks, validation_split=0.2)
scores = model.evaluate(X_Test, Y_Test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])
