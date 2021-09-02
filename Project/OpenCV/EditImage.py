import cv2
import numpy as np

img = np.zeros((360,360,3), np.uint8)
# print(img.shape)
# img[:] = 250,255,157

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #* 3 is for thickness
cv2.rectangle(img,(0,0),(250,300),(0,0,255),cv2.FILLED)
cv2.circle(img,(100,50),30,(255,255,0),3)
cv2.putText(img, "My text", (100,100),cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0),1)

cv2.imshow("Output", img)

cv2.waitKey(5000)