try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import re
tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

# print(pytesseract.image_to_string(Image.open('test.jpg'), lang='eng+kor', config=tessdata_dir_config))

def Function(img):
    img = Image.open(img)

    txt = pytesseract.image_to_string(img, lang='eng+kor', config=tessdata_dir_config)
    txt = txt.replace(" ", "")
    txt = txt.replace("\n", "")
    txt = re.sub('=\)', '', txt)
    print(txt)
    return txt

txt = Function('test.jpg')

