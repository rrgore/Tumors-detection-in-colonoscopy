import os
import shutil
import cv2
import numpy as np
import shutil

SRC_PATH = "/Users/rahulgore/Documents/iai-591/proj3/dataset"
DEST_PATH = "/Users/rahulgore/Documents/iai-591/proj3/class-dataset"
LABEL_PATH = SRC_PATH + "/labels"
INPUT_PATH = SRC_PATH + "/input"
input_files = sorted(os.listdir(INPUT_PATH))
label_files = sorted(os.listdir(LABEL_PATH))
dsize = len(input_files)


for i in range(dsize):
    image = cv2.imread(LABEL_PATH + "/" + label_files[i])
    if len(np.nonzero(image)[0]) > 0:
        shutil.copyfile(
            INPUT_PATH + "/" + input_files[i],
            DEST_PATH + "/1/" + input_files[i]
        )
    else:
        shutil.copyfile(
            INPUT_PATH + "/" + input_files[i],
            DEST_PATH + "/0/" + input_files[i]
        )
