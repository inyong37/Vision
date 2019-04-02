try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import re
tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

def Find_engkor(img):
    img = Image.open(img)
    txt = pytesseract.image_to_string(img, lang='eng+kor', config=tessdata_dir_config)
    txt = txt.replace(" ", "")
    txt = txt.replace("\n", "")
    txt = re.sub('=\)', '', txt)
    return txt

def Find_number(img):
    img = Image.open(img)
    txt = pytesseract.image_to_string(img, config='digits')
    txt = txt.replace(" ", "")
    txt = txt.replace("\n", "")
    txt = re.sub('=\)', '', txt)
    return txt

Table = [
    ['B101', 'B102', 'B103', 'B104', 'B105', 'B106', 'B107', 'B108', 'B109', 'B110'],
    ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111'],
    ['501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511'],
]

# Split with 1
def Split_NGRAM_1(String, N):
    a = zip(*[iter(String)] * N)
    str_ngrams = []
    for ngrams in a:
        str_ngrams.append("".join(ngrams))
    return str_ngrams

# Split with 3
def Split_NGRAM_3(String, N):
    a, b, c = zip(*[iter(String)] * N), zip(*[iter(String[1:])] * N), zip(*[iter(String[2:])] * N)
    str_ngrams = []
    for ngrams in [a, b, c]:
        x = []
        for ngram in ngrams:
            x.append("".join(ngram))
        str_ngrams.append(x)
    return str_ngrams

def Find_Location(String):
    if not String in Table:
        return print('Nope')
    else:
        return print('Yeah')

import cv2 as cv
from PIL import Image
import numpy as np

img_c = cv.imread('Dataset/102.JPG')
#img = cv.imread('501_1.JPG', cv.IMREAD_COLOR)
img_c = cv.cvtColor(img_c, cv.COLOR_BGR2RGB)
img_c = cv.resize(img_c, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv.INTER_AREA) # resize image
img_g = cv.cvtColor(img_c, cv.COLOR_RGB2GRAY)
img_r = cv.bitwise_not(img_g) # color reverse
img_p = Image.fromarray(img_g) # PIL image
img_n = np.asarray(img_p) # numpy image
cv.imwrite('input.jpg', img_r) # save

txt = Find_engkor('input.jpg')
str = Split_NGRAM_3(txt, 3)
pos = Find_Location(str)

cv.imshow('img_c', img_c)
cv.imshow('img_r', img_r)
cv.waitKey(0)
cv.destroyAllWindows()
