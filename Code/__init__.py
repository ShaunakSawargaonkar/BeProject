from video2Frame import videoToFrame
from DabbaNOCR import dabbaNOCR
from CropImage import cropImage
import os
from PIL import Image


VideoLoc='C:/Users/HP/Desktop/Working EasyOCR_for_boundingbox_nd_Recognition/Video/Video1.mp4'
imagePath='Images\image2.jpg'

# 1 Video to frame
NoOfFrames=videoToFrame(VideoLoc,7)

print("video to frame done")

# 2 Crop the frame
folder_path = "ResultFrame"

ctr=0
for filename in os.listdir(folder_path):
     if filename.endswith(".jpg"):
        ctr+=1
        imagepath = os.path.join(folder_path, filename)
        cropImage(imagepath,ctr)

print("Frames cropped till ticker tape")


# 3 Cropped frame to text
folder_path = "CroppedImages"

FinalString=" "

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        imagepath = os.path.join(folder_path, filename)
        FinalString+=dabbaNOCR(imagepath)
        
print("Final Output Text\n" + FinalString)




