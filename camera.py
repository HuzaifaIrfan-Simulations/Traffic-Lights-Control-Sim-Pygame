import cv2


print("package imported")


# img= cv2.imread("me.jpg")
# cv2.imshow('Output',img)
# cv2.waitKey(0)





cap=cv2.VideoCapture("video.mp4")



while True:
    success, img = cap.read()

    cv2.imshow("test video", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break






