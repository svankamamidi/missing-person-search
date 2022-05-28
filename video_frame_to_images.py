# Program To Read video
# and Extract Frames
import cv2
import os

# Function to extract frames

def frameCapture(path, skipFrameCount):

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    frame_count = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = vidObj.get(cv2.CAP_PROP_FPS) # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
    duration = frame_count/fps
    print("duration", duration)
    print("fps", fps)

    # checks whether frames were extracted
    success = 1
    os.makedirs("video-frames", exist_ok=True)    
    
    #Skip frames if asked
    if skipFrameCount > 0:
        for i in range(skipFrameCount, 0, 1):
            vidObj.read()
    
    while success:

        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        if success:             
            frameTimeSlot = count/fps
            cv2.imwrite("video-frames/frame%f.jpg" % frameTimeSlot, image)

        count += 1

# Driver Code

if __name__ == '__main__':

    # Calling the function

    frameCapture("C:\\Users\\vvankamamidi\\OneDrive - OpenText\\Backup\\PY\\face-recognition-effort\\dataset\\self.mp4", 0)
