import os
from os import path
import shutil

# This program puts the raw dataset back into dataset/

directory = "dataset/negative"
raw_dir = "raw_dataset/no"
i = 1
for image in os.listdir(directory):    
    print("deleting file (no): " + str(i))
    os.remove(os.path.join(directory, image))  
    i = i + 1
for image in os.listdir(raw_dir):    
    shutil.copyfile(os.path.join(raw_dir, image), os.path.join(directory, image))

directory = "dataset/positive"
raw_dir = "raw_dataset/yes"
i = 1
for image in os.listdir(directory):    
    print("deleting file (yes): " + str(i))
    os.remove(os.path.join(directory, image))  
    i = i + 1
for image in os.listdir(raw_dir):    
    shutil.copyfile(os.path.join(raw_dir, image), os.path.join(directory, image))
