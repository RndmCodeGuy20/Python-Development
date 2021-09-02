import cv2
import numpy as np

img = np.zeros((360,360,3), np.uint8)
# print(img.shape)
# img[:] = 250,255,157

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #* 3 is for thickness
cv2.rectangle(img,(0,0),(250,300),(0,0,255),3)

cv2.imshow("Output", img)

cv2.waitKey(5000)