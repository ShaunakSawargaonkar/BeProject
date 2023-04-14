from video2Frame import videoToFrame
from DabbaNOCR import dabbaNOCR
import os
from PIL import Image


VideoLoc='C:/Users/HP/Desktop/Working EasyOCR_for_boundingbox_nd_Recognition/Video/video19.mp4'
imagePath='Images\image2.jpg'

NoOfFrames=videoToFrame(VideoLoc,25)

imageCtr=0
folder_path = "ResultFrame"

FinalString=" "

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        imagepath = os.path.join(folder_path, filename)
        FinalString+=dabbaNOCR(imagepath)
        
print("YPPPPPPPPPPPP\n" + FinalString)
    