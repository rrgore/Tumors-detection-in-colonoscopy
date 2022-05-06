import shutil

VIDEO_NAME = "ShortVD_wp_66"
SRC_PATH = "/Users/rahulgore/Documents/iai-591/proj2/TrainingSet_NewGT/" + VIDEO_NAME + "/GT/"
DEST_PATH = "/Users/rahulgore/Documents/iai-591/proj2/srcCode/labels/"

for i in range(1, 617):
    shutil.copyfile(
        SRC_PATH+VIDEO_NAME+"_frame_"+str(i)+"_GT.tiff",
        DEST_PATH+"label_66_"+str(i).zfill(4)+".tiff"
    )
