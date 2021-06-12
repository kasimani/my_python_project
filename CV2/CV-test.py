import cv2
cam = cv2.VideoCapture(0)
#captureDevice = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Manish Cam', frame)

