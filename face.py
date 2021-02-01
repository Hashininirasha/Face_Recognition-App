import cv2

img = cv2.imread("im/pic.jpg")

cv2.imshow("face", img)
cv2.waitKey(0)