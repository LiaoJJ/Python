# -*- coding: utf-8 -*-
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import hashlib
import os
import shutil

'''
把 data 目录下的每个文件夹内的文件每隔10个，保留一个，保存到 data/newdata/XXX 文件夹下   (XXX即原来的文件夹命名)
'''

data = r'./'

def select(data):
    newdata = os.path.join(data, 'newdata')
    if not os.path.exists(newdata):
        os.mkdir(newdata)

    datalist = os.listdir(data)
    for data_n in datalist:
        if not data_n=='newdata':
            data_n_path = os.path.join(data,data_n)
            if os.path.isdir(data_n_path):
                data_n_list = os.listdir(data_n_path)
                for i,pic in enumerate(data_n_list):
                    if i%10==0:
                        picpath = os.path.join(data_n_path,pic)
                        newfilepath =  os.path.join(newdata, data_n)
                        if not os.path.exists(newfilepath):
                            os.mkdir(newfilepath)
                        print picpath
                        shutil.copy(picpath,newfilepath)

select(data)