import cv2 as cv
import time
import numpy as np

human_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')
cap = cv.VideoCapture("IMG_0058.MOV")

frame_size = np.array([[1920, 1080], [640, 180], [320, 180]])

while True:
    r, frame = cap.read()
    if r:
        start_time = time.time()
        frame = cv.resize(frame, (320, 180))  # Resize frame resolution because of processing time
        #frame = cv.resize(frame, frame_size[2])  # Resize frame resolution because of processing time
        gray_frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)  # Haar Cascade classifier needs a gray scale image
        rects = human_cascade.detectMultiScale(gray_frame)

        end_time = time.time()
        print("Elapsed Time:", end_time - start_time)
        for (x, y, w, h) in rects:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            print("Detected")
        cv.imshow("preview", frame)
    k = cv.waitKey(1)
    if k & 0xFF == ord("q"):  # Exit condition
        break
