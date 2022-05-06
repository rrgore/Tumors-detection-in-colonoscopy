from keras_unet_collection import models
import os
import numpy as np
from sklearn.model_selection import train_test_split
import cv2

WIDTH = 480
HEIGHT = 270

images = []
for filename in os.listdir('/content/input'):
    img = cv2.imread(os.path.join('/content/input', filename))
    if img is not None:
      img = cv2.resize(img, (WIDTH,HEIGHT))          # could throw error, have to check
      images.append(img)

labels = []
for filename in os.listdir('/content/labels'):
    img = cv2.imread(os.path.join('/content/labels', filename))
    if img is not None:
      img = cv2.resize(img, (WIDTH,HEIGHT))          # could throw error, have to check
      labels.append(img)

image_arr = np.asarray(images)
labels_arr = np.asarray(labels)
print(image_arr.shape)
print(labels_arr.shape)