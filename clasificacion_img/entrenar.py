import os
import numpy as np
import matplotlib.pyplot as plt
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Flatten, Dense, Activation, Dropout

images = []
labels = []
directories = [["rubelina/corte/", 0],
               ["rubelina/desarrollo/", 1],
               ["rubelina/semilla/", 2],
               ["rubelina/semillero/", 3]]

for i in range(len(directories)):
    folder = os.listdir(directories[i][0])
    for file in folder:
        if os.path.isfile(os.path.join(directories[i][0], file)) & file.endswith('.jpg'):
            image = plt.imread(directories[i][0]+file)
            images.append(image)
            labels.append(directories[i][1])
            
X = np.array(images)
Y = to_categorical(labels)
X_train, X_test, Y_train, Y_test =  train_test_split(X, Y, test_size=0.2)

cnn = Sequential()
for i in range(6):
    cnn.add(Conv2D(filters=32, kernel_size=(3,3),
                   input_shape=(160,240,3), activation="relu",
                   padding="same"))
    cnn.add(MaxPooling2D(pool_size=(2,2)))
    cnn.add(Flatten())
    cnn.add(Dense(256))
    cnn.add(Activation("relu"))
    cnn.add(Dropout(0.5))
    cnn.add(Dense(4))
    cnn.add(Activation("softmax"))
    cnn.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    Cal = [EarlyStopping(monitor="val_loss", patience=20), 
           ModelCheckpoint(filepath="mod_Rubelina.h5", 
                           monitor="val_loss", 
                           save_best_only=True)]
    cnn.fit(X_train, Y_train, 
            batch_size=128, 
            epochs=20, 
            callbacks=Cal, 
            validation_split=0.1, 
            verbose=1)



