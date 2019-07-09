# -*- coding:utf-8 -*-
# Modified Author: Inyong Hwang
# TPS STN
# Reference
# data load
# https://hulk89.github.io/pytorch/2017/11/23/pytorch-image-loader/
# num_workers slows in windows - github issue
# https://github.com/pytorch/pytorch/issues/12831

import torchvision.datasets as dset
import torchvision.transforms as transforms
import torch
from tqdm import tqdm
import time

if __name__ == '__main__':
    start = time.time()
    dataset = dset.ImageFolder(root='D:/Dataset/OCR/STR/DATA_1v4/CHARACTER/',
                               transform=transforms.Compose([
                                   transforms.Resize(128),
                                   # transforms.Scale(128),
                                   transforms.CenterCrop(128),
                                   transforms.ToTensor(),
                                   transforms.Normalize((0.5, 0.5, 0.5),
                                                        (0.5, 0.5, 0.5)),
                               ]))
    '''
    dataloader = torch.utils.data.DataLoader(dataset,
                                             batch_size=2,
                                             shuffle=True,
                                             num_workers=0)
    '''
    dataloader = torch.utils.data.DataLoader(dataset,
                                             batch_size=2,
                                             shuffle=True)
    end = time.time()
    print(end - start)
    '''
    for i, data in tqdm(enumerate(dataloader)):
        print(data[0].size())
        print(data[1])
    '''
