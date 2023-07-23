import os
import numpy as np
import matplotlib.pyplot as plt
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.models import load_model

images = []
labels = []
directories = [["rubelina/corte/", 0],
               ["rubelina/desarrollo/", 1],
               ["rubelina/semilla/", 2],
               ["rubelina/semillero/", 3]]

def Etiqueta(stage):
    if stage==0:
        return "Corte"
    elif stage==1:
        return "Desarrollo"
    elif stage==2:
        return "Semilla"
    elif stage==3:
        return "Semillero"
    
for i in range(len(directories)):
    folder = os.listdir(directories[i][0])
    for file in folder:
        if os.path.isfile(os.path.join(directories[i][0], file)) &  file.endswith('.jpg'):
            image = plt.imread(directories[i][0]+file)
            images.append(image)
            labels.append(directories[i][1])

X = np.array(images)
Y = to_categorical(labels)
X_train, X_test, Y_train, Y_test =  train_test_split(X, Y, test_size=0.2)

model = load_model("mod_Rubelina.h5")
evaluation = model.evaluate(X_test, Y_test, verbose=1)
print("Precisión del test:", evaluation[1])

prediction = model.predict_classes(X_test)
for i in range(10):
    plt.imshow(X_test[i])
    plt.title(f"Etiqueta: {Etiqueta (np.argmax(Y_test[i]))} \nClasificación: {Etiqueta(prediction[i])}")
    plt.show()

