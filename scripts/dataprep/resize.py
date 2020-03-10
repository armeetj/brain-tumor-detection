import os
from os import path
import cv2

# this program resizes all images and tries to normalize all images to preapre for training
dimensions = (300, 300)
directory = "dataset/negative"
i = 1
for image in os.listdir(directory):    
    print("resizing file (no): " + str(i))
    img = cv2.imread(os.path.join(directory, image), cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(img, dimensions)
    cv2.imwrite(os.path.join(directory, image),resized)
    i = i + 1

directory = "dataset/positive"
i = 1
for image in os.listdir(directory):    
    print("resizing file (yes): " + str(i))
    img = cv2.imread(os.path.join(directory, image), cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(img, dimensions)
    cv2.imwrite(os.path.join(directory, image),resized)
    i = i + 1