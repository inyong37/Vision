# Description       : Support Vector Machine in OpenCV
# (Modified) Author : Inyong Hwang (inyong1020@gmail.com)
# Data              : 2020-07-10-Fri
# Reference         : https://docs.opencv.org/master/d1/d73/tutorial_introduction_to_svm.html


import cv2 as cv
import numpy as np

# Set up training data
labels = np.array([1, -1, -1, -1])
trainingData = np.matrix([[501, 10], [255, 10], [501, 255], [10, 501]], dtype=np.float32)

# Train the SVM
svm = cv.ml.SVM_create()
svm.setType(cv.ml.SVM_C_SVC)
svm.setKernel(cv.ml.SVM_LINEAR)
svm.setTermCriteria((cv.TERM_CRITERIA_MAX_ITER, 100, 1e-6))
svm.train(trainingData, cv.ml.ROW_SAMPLE, labels)

# Data for visual representation
width = 512
height = 512
image = np.zeros((height, width, 3), dtype=np.uint8)

# Show the decision regions given by the SVM
green = (0, 255, 0)
blue = (255, 0, 0)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        sampleMat = np.matrix([[j, i]], dtype=np.float32)
        response = svm.predict(sampleMat)[1]
        if response == 1:
            image[i, j] = green
        elif response == -1:
            image[i, j] = blue

# Show the training data
thickness = -1
cv.circle(image, (501,  10), 5, (0,   0,   0), thickness)
cv.circle(image, (255,  10), 5, (255, 255, 255), thickness)
cv.circle(image, (501, 255), 5, (255, 255, 255), thickness)
cv.circle(image, (10, 501), 5, (255, 255, 255), thickness)

# Show support vectors
thickness = 2
sv = svm.getUncompressedSupportVectors()
for i in range(sv.shape[0]):
    cv.circle(image, (sv[i, 0], sv[i, 1]), 6, (128, 128, 128), thickness)
# save the image
cv.imwrite('result.png', image)
# show it to the user
cv.imshow('SVM Simple Example', image)
cv.waitKey()
