import cv2

img = cv2.imread("D:\Python Development\Resource\Images\1138974.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #* Image Gray
imgBlur = cv2.GaussianBlur(img,(7,7),0) #* Image Blur
imgCanny = cv2.Canny(img, 100,100)

cv2.imshow("Gray Image Output",imgGray)
cv2.imshow("Canny Image Output",imgCanny)
cv2.imshow("Blur Image Output",imgBlur)

cv2.waitKey(10000)