import cv2

cap = cv2.VideoCapture("D:\Python Development\Resource\Images\lagreca-busted-open.gif")

while True:
    success, img = cap.read()
    cv2.imshow("Video Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 