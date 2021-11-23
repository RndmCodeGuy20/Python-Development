import cv2

path = "D:\Python Development\Resource\Images\siyuan-hDzllryPB9g-unsplash.jpg"
img = cv2.imread(path)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original", img)
cv2.imshow("HSV Output", imgHSV)

cv2.waitKey(5000)
