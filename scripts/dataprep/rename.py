import os
from os import path

# This program quickly renames all data files to #.jpg in the yes/ and no/ folders of dataset/

directory = "dataset/no"
i = 1
for image in os.listdir(directory):    
    print("converting file (no): " + str(i))
    print(image)
    os.rename(os.path.join(directory, image), os.path.join(directory, str(i) + ".jpg"))
    print(image)
    i = i + 1

directory = "dataset/yes"
i = 1
for image in os.listdir(directory):    
    print("converting file (yes): " + str(i))
    print("before: " + image)
    os.rename(os.path.join(directory, image), os.path.join(directory, str(i) + ".jpg"))
    i = i + 1
