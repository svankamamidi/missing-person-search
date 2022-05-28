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
while success:
    #generate next 5000 frame jpegs
    shortLoopIndex = shortLoopSize
    os.makedirs("video-frames", exist_ok=True)
    
    while success and shortLoopIndex > 0:
        success, image = vidObj.read()

        # Saves the frames with frame-count
        if success: 
            frameTimeSlot = count/fps
            cv2.imwrite("video-frames/frame%f.jpg" % frameTimeSlot, image)
        count += 1
        shortLoopIndex -= 1
    
    for (root, dirs, file) in os.walk(photoTOMatchPath):
        for comparedPicName in file:
            print("File being matched ", comparedPicName)

            for (root, dirs, file) in os.walk(videoFramesPathSlash):
                for framePicName in file:
                    try:
                        result = DeepFace.verify(img1_path = photoTOMatchPath + str(comparedPicName),
                                                 img2_path = videoFramesPathSlash + str(framePicName))

                        if result["verified"]:
                            print("matched ", videoFramesPathSlash + str(framePicName))
                            #TODO: copy matched frame to matched folder
                            os.makedirs("matched-frames", exist_ok=True)
                            shutil.copyfile(videoFramesPathSlash + str(framePicName), "matched-frames/" + str(framePicName))
                            #print(result)
                        else:
                            print("no match", videoFramesPathSlash + str(framePicName))
                        #print(result["verified"])                    
                    except:
                        pass
    shutil.rmtree(videoFramesPath)
