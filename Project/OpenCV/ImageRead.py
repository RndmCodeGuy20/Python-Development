import cv2

img = cv2.imread("D:\Python Development\Resource\Images\MultipleInherit.png")

n = int(input("Enter the amount of time you want to see the image : "))

cv2.imshow("Output", img)
cv2.waitKey(n)
