import numpy as np
import cv2 as cv

x = 1024
y = 512

img = np.zeros((y, x, 3), np.uint8)
cv.rectangle(img, (0, 0), (x, y), (255, 255, 255), y)
font = cv.FONT_HERSHEY_SIMPLEX

# B101
cv.rectangle(img, (int(6.5/8*x), int(3.5/5*y)), (x, y), (0, 0, 0), 4)
cv.putText(img, 'B101', (int(6.5/8*x)+5, int(3.5/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B102
cv.rectangle(img, (int(4.5/8*x), int(3.5/5*y)), (x, y), (0, 0, 0), 4)
cv.putText(img, 'B102', (int(4.5/8*x)+5, int(3.5/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B103
cv.rectangle(img, (int(3.5/8*x), int(3.5/5*y)), (x, y), (0, 0, 0), 4)
cv.putText(img, 'B103', (int(3.5/8*x)+5, int(3.5/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B104
cv.rectangle(img, (int(2/8*x), int(3.5/5*y)), (x, y), (0, 0, 0), 4)
cv.putText(img, 'B104', (int(2/8*x)+5, int(3.5/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B105
cv.rectangle(img, (int(1/15*x), int(3.5/5*y)), (int(2/8*x), y), (0, 0, 0), 4)
cv.putText(img, 'B105', (int(1/15*x)+5, int(3.5/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B106
cv.rectangle(img, (0, int(2/5*y)), (int(2/15*x), int(3/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B106', (5, int(2/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B107
cv.rectangle(img, (0, int(1/5*y)), (int(2/15*x), int(2/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B107', (5, int(1/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B108
cv.rectangle(img, (int(2/15*x), int(1/5*y)), (int(2/8*x), int(2/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B108', (int(2/15*x)+5, int(1/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B109
cv.rectangle(img, (0, 0), (int(2/8*x), int(1/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B109', (5, 30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B110
cv.rectangle(img, (int(2.7/8*x), 0), (int(4/8*x), int(1/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B110', (int(2.7/8*x)+5, 30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B111
cv.rectangle(img, (int(2.7/8*x), int(2/5*y)), (int(3.5/8*x), int(2.5/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B111', (int(2.7/8*x)+5, int(2/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B111A
cv.rectangle(img, (int(2.7/8*x), int(1/5*y)), (int(3.5/8*x), int(2/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B111A', (int(2.7/8*x)+5, int(1/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B112
cv.rectangle(img, (int(4/8*x), 0), (int(5.3/8*x), int(1/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B112', (int(4/8*x)+5, 30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B113
cv.rectangle(img, (int(6/8*x), 0), (x, int(1/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B113', (int(6/8*x)+5, 30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B114
cv.rectangle(img, (int(13/15*x), int(2/5*y)), (x, int(3/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B114', (int(13/15*x)+5, int(2/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B115
cv.rectangle(img, (int(13/15*x), int(1/5*y)), (x, int(2/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B115', (int(13/15*x)+5, int(1/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)
# B116
cv.rectangle(img, (int(6/8*x), int(1/5*y)), (x, int(2/5*y)), (0, 0, 0), 4)
cv.putText(img, 'B116', (int(6/8*x)+5, int(1/5*y)+30), font, 1, (0, 0, 0), 2, cv.LINE_AA)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()