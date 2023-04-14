import cv2

def videoToFrame(videoPath,time_interval):
    # videoPath='C:/Users/HP/Desktop/Working EasyOCR_for_boundingbox_nd_Recognition/Video/video19.mp4'
    video = cv2.VideoCapture(videoPath)

    # Define the time interval in seconds
    # time_interval = 3.5

    noOfFrames=0
    # Set the frame count and the current time to zero
    frame_count = 0
    current_time = 0
    folderpath= "C:\\Users\\HP\\Desktop\\Working EasyOCR_for_boundingbox_nd_Recognition\\ResultFrame\\ResultFrame"
        
    while True:
        # Read a frame from the video
        ret, frame = video.read()

        # Check if a frame was successfully captured
        if not ret:
            break

        # Increment the frame count and the current time
        frame_count += 1
        current_time += 1 / video.get(cv2.CAP_PROP_FPS)

        # Check if the current time is greater than the time interval
        if current_time > time_interval:
            # Save the current frame as an image
            cv2.imwrite(str(folderpath) + 'frame{}.jpg'.format(noOfFrames), frame)
            # cv2.imwrite(str(folderpath) + 'frame%d.jpg' % frame_count, frame)

            noOfFrames+=1
            # Reset the current time
            current_time = 0

    # Release the video file
    video.release()
    return noOfFrames


