from PIL import Image  # Import Image class from library.

def cropImage(imagePath,ctrInt):
    # TEST
    # imagePath="C:\\Users\\HP\\Desktop\\Working EasyOCR_for_boundingbox_nd_Recognition\\Images\\Screenshot.jpg"
    # ctrInt=5

    ctr=str(ctrInt)
    folderpath="C:/Users/HP/Desktop/Working EasyOCR_for_boundingbox_nd_Recognition/CroppedImages/"

    # Load image.
    image = Image.open(imagePath) 

    width, height = image.size
    #TODO
    #hard coding here
    crop_height = int(0.97 * height) 
    top = 0.93 * height 
    left=width * 0.16
    right= width * 0.88
    # set the dimensions of the crop box (left, upper, right, lower)
    cropped_image = image.crop((left, top, right, crop_height))  # Crop the image.

    cropped_image.save(folderpath + ctr + ".jpg")  



# from PIL import Image  # Import Image class from library.

# folderpath="C:/Users/HP/Desktop/Working EasyOCR_for_boundingbox_nd_Recognition/CroppedImages/"
# imagePath="C:\\Users\\HP\\Desktop\\Working EasyOCR_for_boundingbox_nd_Recognition\\Images\\image.jpg"
# image = Image.open(imagePath)  # Load image.

# width, height = image.size
# ctr="1"
# top = height * 2 // 3
# bottom = height
# # set the dimensions of the crop box (left, upper, right, lower)
# cropped_image = image.crop((0, top, width, bottom))  # Crop the image.

# cropped_image.save(folderpath + ctr + ".jpg")  