# Program To Read video
# and Extract Frames
import cv2
import os

vidObj = cv2.VideoCapture("C:\\Users\\vvankamamidi\\OneDrive - OpenText\\Backup\\PY\\face-recognition-effort\\dataset\\self.mp4")
frame_count = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidObj.get(cv2.CAP_PROP_FPS)
duration = frame_count/fps
def getFrame(sec): 
    vidObj.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
    hasFrames,image = vidObj.read() 
    if hasFrames: 
        cv2.imwrite("video-frames/frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file 
    return hasFrames 

sec = 0 
frameRate = 0.25 #it will capture image in each 0.5 second 
success = getFrame(sec) 
while success and sec <= duration: 
    sec = sec + frameRate 
    sec = round(sec, 2) 
    success = getFrame(sec)
    
# Function to extract frames
