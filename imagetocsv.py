from PIL import Image
import numpy as np
import os
import csv

# default format can be changed as needed
def createFileList(myDir, format='.jpg'):
    fileList = []
    # print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

# load the original image
myFileList = createFileList('emotion\model')

for file in myFileList:
    print(file)
    img_file = Image.open(file)
    # img_file.show()

    # Make image Greyscale
    img_grey = img_file.convert('L')
    # img_grey.show()

    # Resize pixel to 48x48
    img = img_grey.resize((48,48), Image.ANTIALIAS)
    # img.show()
   
    # Save img resize to Array
    value = np.asarray(img)
    ressu = value.flatten()
    print(ressu)
    with open("emotion\data.csv", 'a', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow(ressu)