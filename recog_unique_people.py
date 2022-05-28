import os, shutil
import cv2
from deepface import DeepFace
from video_frame_to_images import frameCapture

videoFilePath = "C:/Users/vvankamamidi/OneDrive - OpenText/Backup/PY/face-recognition-effort/dataset/self.mp4"
videoFramesPath = "C:/Users/vvankamamidi/OneDrive - OpenText/Backup/PY/face-recognition-effort/video-frames"
videoFramesPathSlash = videoFramesPath + str("/")
uniquePhotos = "uniquePhotos"

#read video
#for every 5 mins (around 5000 frames) generate frames and analyze/detect for match them and delete them and move to next 5 mins (~5000 frames)
success = 1
shortLoopSize = 3600 #seconds
vidObj = cv2.VideoCapture(videoFilePath)
frame_count = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
fps = vidObj.get(cv2.CAP_PROP_FPS) # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
duration = frame_count/fps
print("duration", duration)
print("fps", fps)
os.makedirs(uniquePhotos, exist_ok=True)
def getFrame(sec): 
    vidObj.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
    hasFrames,image = vidObj.read() 
    if hasFrames: 
        cv2.imwrite("video-frames/frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file
        if sec == 0:
            cv2.imwrite(uniquePhotos + "/frame "+str(sec)+" sec.jpg", image)
    return hasFrames

sec = 0 
frameRate = 0.25 #it will capture image in each 0.25 second 
while success and sec <= duration:
    #generate next 5000 frame jpegs
    shortLoopIndex = shortLoopSize
    os.makedirs("video-frames", exist_ok=True)
    success = getFrame(sec)
    
    while success and shortLoopIndex > 0 and sec <= duration:
        sec = sec + frameRate 
        sec = round(sec, 2) 
        success = getFrame(sec)
        shortLoopIndex -= 1
    
    print("success " + str(success) + " seconds " + str(sec))
    for (root, dirs, file) in os.walk(uniquePhotos):
        for comparedPicName in file:
            print("File being matched ", comparedPicName)

            for (root, dirs, file) in os.walk(videoFramesPathSlash):
                for framePicName in file:
                    try:
                        result = DeepFace.verify(img1_path = uniquePhotos + str(comparedPicName),
                                                 img2_path = videoFramesPathSlash + str(framePicName))

                        if result["verified"]:
                            print("matched ", videoFramesPathSlash + str(framePicName))
                            #TODO: copy matched frame to matched folder
                            os.makedirs("matched-frames", exist_ok=True)
                            
                            #print(result)
                        else:
                            print("found unique person ", videoFramesPathSlash + str(framePicName))
                            shutil.copyfile(videoFramesPathSlash + str(framePicName), uniquePhotos + "/" + str(framePicName))
                    except:
                        pass
    shutil.rmtree(videoFramesPath)
