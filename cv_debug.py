import os, shutil
import cv2
from deepface import DeepFace
from video_frame_to_images import frameCapture

videoFilePath = "C:/Users/vvankamamidi/OneDrive - OpenText/Backup/PY/face-recognition-effort/dataset/self.mp4"
videoFramesPath = "C:/Users/vvankamamidi/OneDrive - OpenText/Backup/PY/face-recognition-effort/video-frames"
videoFramesPathSlash = videoFramesPath + str("/")
photoTOMatchPath = "C:/Users/vvankamamidi/Pictures/"

#read video
#for every 5 mins (around 5000 frames) generate frames and analyze/detect for match them and delete them and move to next 5 mins (~5000 frames)
count = 0
success = 1
shortLoopSize = 5000
vidObj = cv2.VideoCapture(videoFilePath)
frame_count = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidObj.get(cv2.CAP_PROP_FPS) # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
duration = frame_count/fps
print("duration", duration)
print("fps", fps)