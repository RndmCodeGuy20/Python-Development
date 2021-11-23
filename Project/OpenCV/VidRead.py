import cv2

cap = cv2.VideoCapture(
    "D:\Python Development\Resource\Images\crowd-of-people-walking-815307-PREVIEW.mp4"
)

while True:
    success, img = cap.read()
    cv2.imshow("Video Output", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break