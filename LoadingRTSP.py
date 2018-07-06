import cv2 as cv

vcap = cv.VideoCapture("rtsp://admin:1qazxsw2!QAZXSW@@datascience.opswerx.org:20052")
while(1):
    ret, frame = vcap.read()
    cv.imshow('VIDEO', frame)
    cv.waitKey(1)