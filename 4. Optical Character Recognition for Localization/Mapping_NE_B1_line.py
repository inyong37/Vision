import numpy as np
import cv2 as cv

img = np.zeros((512, 1024, 3), np.uint8)
img = cv.line(img, (0, 0), (1024, 0), (255, 255, 255), 1024)

x = 1023
y = 511

y1 = int(1/5*y)
y2 = int(2/5*y)
y3 = int(3/5*y)
y4 = int(4/5*y)
y5 = int(3.5/5 * y)
y2_5 = int(2.5/5*y)

x1 = int(1/8*x)
x2 = int(2/8*x)
x3 = int(3/8*x)
x4 = int(4/8*x)
x5 = int(5/8*x)
x6 = int(6/8*x)
x7 = int(7/8*x)
x8 = int(1/15*x)
x3_5 = int(3.5 / 8 * x)
x4_5 = int(4.5 / 8 * x)
x6_5 = int(6.5/8*x)
# 1
# x
img = cv.line(img, (0, y1), (x2, y1), (0, 0, 0), 5)
img = cv.line(img, (x3, y1), (x5, y1), (0, 0, 0), 5)
img = cv.line(img, (x6, y1), (x, y1), (0, 0, 0), 5)
# y
img = cv.line(img, (x2, 0), (x2, y1), (0, 0, 0), 5)
img = cv.line(img, (x3, 0), (x3, y1), (0, 0, 0), 5)
img = cv.line(img, (x4, 0), (x4, y1), (0, 0, 0), 5)
img = cv.line(img, (x5, 0), (x5, y1), (0, 0, 0), 5)
img = cv.line(img, (x6, 0), (x6, y1), (0, 0, 0), 5)

# 2
# x
img = cv.line(img, (0, y5), (x, y5), (0, 0, 0), 5)
# y
img = cv.line(img, (x8, y5), (x8, y), (0, 0, 0), 5)
img = cv.line(img, (x2, y5), (x2, y), (0, 0, 0), 5)
img = cv.line(img, (x3_5, y5), (x3_5, y), (0, 0, 0), 5)
img = cv.line(img, (x4_5, y5), (x4_5, y), (0, 0, 0), 5)
img = cv.line(img, (x6_5, y5), (x6_5, y), (0, 0, 0), 5)

# 3
# x 1
img = cv.line(img, (0, y2), (x2, y2), (0, 0, 0), 5)
img = cv.line(img, (x3, y2), (x4, y2), (0, 0, 0), 5)
img = cv.line(img, (x6, y2), (x, y2), (0, 0, 0), 5)
# x 2
img = cv.line(img, (0, y3), (x2, y3), (0, 0, 0), 5)
img = cv.line(img, (x3, y2_5), (x4, y2_5), (0, 0, 0), 5)
img = cv.line(img, (x6, y3), (x, y3), (0, 0, 0), 5)
# y
img = cv.line(img, (x1, y1), (x1, y3), (0, 0, 0), 5)
img = cv.line(img, (x2, y1), (x2, y3), (0, 0, 0), 5)
img = cv.line(img, (x3, y1), (x3, y2_5), (0, 0, 0), 5)
img = cv.line(img, (x4, y1), (x4, y2_5), (0, 0, 0), 5)
img = cv.line(img, (x6, y1), (x6, y3), (0, 0, 0), 5)
img = cv.line(img, (x7, y1), (x7, y3), (0, 0, 0), 5)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
