# -*- coding: utf-8 -*-
"""CNNPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/191b18vMin-QPRtPeRajL2spRDW9RF_Y5
"""

from tensorflow.keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import numpy as np

model = load_model("mnistCNN.h5")

img = Image.open("C:/Users/Dell/PycharmProjects/A-novel-method-for-digit-recognition-system/data/1.png").convert("L") # convert image to monochrome
img = img.resize( (28,28) ) # resizing of input image

img

im2arr = np.array(img) #converting to image
im2arr = im2arr.reshape(1, 28, 28, 1) #reshaping according to our requirement

pred = model.predict(im2arr)
print(pred)

num = np.argmax(pred, axis=1) #printing our Labels
print(num[0])