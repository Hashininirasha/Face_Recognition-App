import cv2

video = cv2.VideoCapture(0)
while True:
    success,img=video.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        break