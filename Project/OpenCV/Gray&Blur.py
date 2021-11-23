import cv2
import numpy as np

img = cv2.imread(
    "D:\Python Development\Resource\Images\wallpapersden.com_spider-man-pixel-art_360x360.jpg"
)
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # ` Image Gray
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)  # ` Image Blur
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Gray Image Output", imgGray)
cv2.imshow("Canny Image Output", imgCanny)
cv2.imshow("Blur Image Output", imgBlur)
cv2.imshow("Dilation Image Output", imgDilation)
cv2.imshow("Eroded Image Output", imgEroded)


cv2.waitKey(1500)