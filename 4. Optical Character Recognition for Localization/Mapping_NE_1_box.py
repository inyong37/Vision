import numpy as np
import cv2 as cv

x = 1024
y = 512

img = np.zeros((y, x, 3), np.uint8)
cv.rectangle(img, (0, 0), (x, y), (255, 255, 255), y)
font = cv.FONT_HERSHEY_SIMPLEX

# 101
cv.rectangle(img, (int(11/13*x), int(3.5/5*y)), (x, y), (0, 0, 0), 4)
cv.putText(img, '101', (int(11/13*x), int(3.5/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 102
cv.rectangle(img, (int(9/13*x), int(3.5/5*y)), (int(11/13*x), y), (0, 0, 0), 4)
cv.putText(img, '102', (int(9/13*x), int(3.5/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 103
cv.rectangle(img, (int(2/13*x), int(3.5/5*y)), (int(4/13*x), y), (0, 0, 0), 4)
cv.putText(img, '103', (int(2/13*x), int(3.5/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 104
cv.rectangle(img, (0, int(3.5/5*y)), (int(2/13*x), y), (0, 0, 0), 4)
cv.putText(img, '104', (0, int(3.5/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 105
cv.rectangle(img, (0, 0), (int(1.5/13*x), int(3/5*y)), (0, 0, 0), 4)
cv.putText(img, '105', (0, int(3/5*y)-10), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 106
cv.rectangle(img, (int(1.5/13*x), 0), (int(3/13*x), int(1.5/5*y)), (0, 0, 0), 4)
cv.putText(img, '106', (int(1.5/13*x), int(1.5/5*y)-10), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 107
cv.rectangle(img, (int(4/13*x), 0), (int(6/13*x), int(1.5/5*y)), (0, 0, 0), 4)
cv.putText(img, '107', (int(4/13*x), int(1.5/5*y)-10), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 108
cv.rectangle(img, (int(6/13*x), 0), (int(8/13*x), int(1.5/5*y)), (0, 0, 0), 4)
cv.putText(img, '108', (int(6/13*x), int(1.5/5*y)-10), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 109
cv.rectangle(img, (int(8/13*x), 0), (int(9/13*x), int(1/5*y)), (0, 0, 0), 4)
cv.putText(img, '109', (int(8/13*x), int(1/5*y)-10), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 110 111 112
cv.rectangle(img, (int(9/13*x), 0), (int(x), int(1.5/5*y)), (0, 0, 0), 4)
cv.putText(img, '110 111 112', (int(9/13*x), int(1.5/5*y)-10), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# 113
cv.rectangle(img, (int(12.3/13*x), int(1.5/5*y)), (int(x), int(2.25/5*y)), (0, 0, 0), 4)
cv.putText(img, '113', (int(12.3/13*x), int(2.25/5*y)-10), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# center
cv.rectangle(img, (int(12.3/13*x), int(2.25/5*y)), (int(x), int(3/5*y)), (0, 0, 0), 4)
# 114
cv.rectangle(img, (int(11.3/13*x), int(1.5/5*y)), (int(12/13*x), int(2.25/5*y)), (0, 0, 0), 4)
cv.putText(img, '114', (int(11.3/13*x), int(2.25/5*y)-10), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# MDF
cv.rectangle(img, (int(11.3/13*x), int(2.25/5*y)), (int(12/13*x), int(3/5*y)), (0, 0, 0), 4)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
