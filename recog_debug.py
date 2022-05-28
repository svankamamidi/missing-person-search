import os
from deepface import DeepFace
from video_frame_to_images import frameCapture

videoFramesPath = "C:/Users/vvankamamidi/OneDrive - OpenText/Backup/PY/face-recognition-effort/video-frames/"
photoTOMatchPath = "C:/Users/vvankamamidi/Pictures/"

for (root, dirs, file) in os.walk(photoTOMatchPath):
    for comparedPicName in file:
        print("File being matched ", comparedPicName)

        for (root, dirs, file) in os.walk(videoFramesPath):
            for framePicName in file:
                try:
                    result = DeepFace.verify(img1_path = photoTOMatchPath + str(comparedPicName),
                                             img2_path = videoFramesPath + str(framePicName))

                    if result["verified"]:
                        print("matched ", videoFramesPath + str(framePicName))
                        #print(result)
                    else:
                        print("no match", videoFramesPath + str(framePicName))
                    #print(result["verified"])                    
                except:
                    pass
