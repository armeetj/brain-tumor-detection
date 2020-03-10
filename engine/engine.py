#imports

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

from tensorflow.keras import datasets, layers, models, optimizers
from keras_preprocessing.image import ImageDataGenerator

import matplotlib.pyplot as plt

CLASS_NAMES = ['negative', 'positive']
train_images = []
train_labels = []
test_images = []
test_labels = []
valid_images = []
valid_labels = []

DIM = 300
train_path = "dataset/train"
valid_path = "dataset/valid"
test_path = "dataset/test"

train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(DIM,DIM), classes=CLASS_NAMES, batch_size=10)
valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(DIM,DIM), classes=CLASS_NAMES, batch_size=10)
test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(DIM,DIM), classes=CLASS_NAMES, batch_size=1)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation = 'relu', input_shape=(DIM, DIM, 3)),
    layers.MaxPooling2D((2, 2)),
    #layers.Conv2D(32, (3, 3), activation = 'relu', input_shape=(DIM, DIM, 3)),
    #layers.MaxPooling2D((2, 2)),
    #layers.Conv2D(32, (3, 3), activation = 'relu', input_shape=(DIM, DIM, 3)),
    layers.Flatten(),
    layers.Dense(2, activation='relu')

])

print(model.summary())

model.compile(optimizers.Adam(lr=0.0000000001), loss='binary_crossentropy', metrics=['accuracy'])

model.fit_generator(train_batches, steps_per_epoch=1, validation_data=valid_batches, validation_steps=1, epochs=200, verbose=2)

test_images, test_labels = next(test_batches)
