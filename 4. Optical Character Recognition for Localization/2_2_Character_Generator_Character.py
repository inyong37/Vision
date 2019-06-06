# -*- coding:utf-8 -*-
# Author : Inyong Hwang
# 2-1. Generating Character, Directory by Fonts

import dict
import os
from tqdm import tqdm
from PIL import Image, ImageFont, ImageDraw

new = dict.character_encoding()
character = list(new.keys())

fonts_directory = 'D:/Dataset/OCR/STR/DATA_1v2/FONT'

ttc_directory = fonts_directory + '/TTC'
ttc_fonts = []
ttcs = os.listdir(ttc_directory)
for ttc in ttcs:
    ttc_fonts.append(ttc_directory + '/' + ttc)

ttf_directory = fonts_directory + '/KOREAN'
ttf_fonts = []
ttfs = os.listdir(ttf_directory)
for ttf in ttfs:
    ttf_fonts.append(ttf_directory + '/' + ttf)

font_size = 44
image_size = [64, 64]

for i in tqdm(range(0, len(character))):
    char_dir = hex(ord(character[i]))
    save_dir = str(ttc_directory).replace('_1v2', '_1v3').replace('FONT/TTC', 'CHARACTER/' + char_dir)
    # print(save_dir)
    if os.path.isdir(save_dir):
        pass
    else:
        os.mkdir(save_dir)

    # ttc
    for j in range(0, len(ttc_fonts)):
        image = Image.new('RGB', size=image_size, color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(ttc_fonts[j], font_size)
        draw.text((10, 10), character[i], font=font, fill='black')
        image_path = save_dir + '/' + ttcs[j].replace('.ttc', '_') + hex(ord(character[i])) + '.png'
        # print(image_path)
        image.save(image_path)
    # ttf
    for k in range(0, len(ttf_fonts)):
        image = Image.new('RGB', size=image_size, color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(ttf_fonts[k], font_size)
        draw.text((10, 10), character[i], font=font, fill='black')
        image_path = save_dir + '/' + ttfs[k].replace('.ttf', '_') + hex(ord(character[i])) + '.png'
        # print(image_path)
        image.save(image_path)
