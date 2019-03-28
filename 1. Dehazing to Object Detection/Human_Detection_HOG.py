import cv2 as cv
import time

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
cap = cv.VideoCapture("IMG_0054.MOV")
while True:
    r, frame = cap.read()
    if r:
        start_time = time.time()
        # frame = cv.resize(frame, (1280, 720))  # Resize frame resolution to 1280*720 because of processing time
        frame = cv.resize(frame, (640, 360))  # Resize frame resolution to 640*360 because of processing time
        # frame = cv.resize(frame, (320, 180))  # Resize frame resolution to 320*180 because of processing time
        gray_frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)  # HOG needs a gray scale image

        rects, weights = hog.detectMultiScale(gray_frame)

        # Measure elapsed time for detections
        end_time = time.time()
        print("Elapsed time:", end_time - start_time)

        for i, (x, y, w, h) in enumerate(rects):
            if weights[i] < 0.7:
                continue
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv.imshow("preview", frame)
    k = cv.waitKey(1)
    if k & 0xFF == ord("q"):  # Exit condition
        break
