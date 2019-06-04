def vgg19(classes):
    i = Input(shape=train_image.shape[1:], name='Input_Image')

    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='Conv1_1')(i)
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='Conv1_2')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool1')(x)

    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='Conv2_1')(x)
    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='Conv2_2')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool2')(x)

    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='Conv3_1')(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='Conv3_2')(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='Conv3_3')(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='Conv3_4')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool3')(x)

    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv4_1')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv4_2')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv4_3')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv4_4')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool4')(x)

    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv5_1')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv5_2')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv5_3')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv5_4')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool5')(x)

    x = Flatten(name='flatten')(x)
    x = Dense(4096, activation='relu', name='fc1')(x)
    x = Dense(4096, activation='relu', name='fc2')(x)
    # 4096: OOM
    # 4: loss, acc, val_loss, val_acc fixed
    y = Dense(classes, activation='softmax', name='predictions')(x)
    model = Model(inputs=i, outputs=y, name='vgg19')
    return model
