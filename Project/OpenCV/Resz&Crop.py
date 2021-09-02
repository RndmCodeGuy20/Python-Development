import cv2
import numpy as np

img = cv2.imread("D:\Python Development\Resource\Images\wallpapersden.com_spider-man-pixel-art_360x360.jpg")
print(img.shape)

imgResize = cv2.resize(img, (480,480))
print(imgResize.shape)

imgCropped = img[]

cv2.imshow("Image Output", img)
cv2.imshow("Resized Image Output", imgResize)

cv2.waitKey(10000)
