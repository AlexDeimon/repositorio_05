from PIL import Image
import os

path = "C:/Users/DIEGO/Downloads/Cafe/entrenamiento/PlagaMinador"

def resize_aspect_fit():
    dirs = os.listdir(path)
    for item in dirs:
        if os.path.isfile(path+item):
            image = Image.open(path+item)
            file_path, extension = os.path.splitext(path+item)

            image = image.resize((240, 160), Image.ANTIALIAS)
            image.save(file_path + "_small" + extension, 'JPEG', quality=90)


resize_aspect_fit()