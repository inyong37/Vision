# -*- coding:utf-8 -*-
# Author : Inyong Hwang
# 1. Making Korean Dictionary based on Distribution by Korean

import pandas as pd
from tqdm import tqdm
import re
from collections import Counter
import operator
from string import ascii_letters


def character_encoding():
    file = 'D:/Dataset/OCR/STR/DATA_1v3/KOREAN_DICTIONARY.txt'

    data = pd.read_csv(file, sep='\t')
    data = data['단어']

    for i in tqdm(range(0, len(data))):
        data[i] = re.sub('[^가-힣]+', '', data[i])

    '''
    C:/Users/terry/Desktop/Project/Vision/4. Optical Character Recognition for Localization/STR/1_DATA_CODE_v3/1_Korean_Dictionary_Korean.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      # 1. Making Korean Dictionary based on Distribution by Korean
    '''

    unigram = []
    for i in range(0, len(data)):
        ngrams = zip(*[iter(data[i])])
        for ngram in ngrams:
            unigram.append(''.join(ngram))

    cnt = Counter(unigram)
    cnt.most_common()
    cnt = sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)

    New = {}
    for i in range(0, 10):
        New[str(i)] = i + 1

    English = list(ascii_letters)
    for i in range(11, 63):
        New[English[i - 11]] = i

    for i, content in enumerate(cnt):
        New[content[0]] = i + 63

    return New
