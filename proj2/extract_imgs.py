import cv2
import os


INPUT_NUMBER = '66'
VIDEO_PREFIX = 'ShortVD_wp_' + INPUT_NUMBER
PATH = "/Users/rahulgore/Documents/iai-591/proj2/TrainingSet_NewGT/" + VIDEO_PREFIX + "/" + VIDEO_PREFIX + ".wmv"


capture = cv2.VideoCapture(PATH)
 
frameNr = 1
os.chdir('input')
while (True): 
    success, frame = capture.read() 
    if success:
        cv2.imwrite("image_"+INPUT_NUMBER+"_"+str(frameNr).zfill(4)+".jpg", frame) 
    else:
        break 
    frameNr = frameNr+1


capture.release()
os.chdir('..')