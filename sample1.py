from deepface import DeepFace

#result = DeepFace.verify(img1_path = "dataset/img1.jpg", img2_path = "dataset/img2.jpg", distance_metric = "euclidean_l2")

result = DeepFace.verify(img1_path = "C:\\Users\\vvankamamidi\\OneDrive - OpenText\\Backup\PY\\face-recognition-effort\\video-frames\\frame35.jpg",
                         img2_path = "C:\\Users\\vvankamamidi\\Pictures\\Capture.jpg")

#verification = result[1]

#if verification:
#    print("match")
#else:
#    print("no match")
#print(result["verified"])
print(result)
