# -*- coding: utf-8 -*-
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import hashlib
import os
import shutil

'''
遍历该文件夹下所有文件夹、子文件夹、及文件，若发现size小于300x300的.jpg文件，则对其进行删除操作
'''

# True-filtered   False-reserved
def filter(filepath,filter_type,filter_size):
    if os.path.splitext(filepath)[1] == filter_type:
        image = mpimg.imread(filepath)
        if len(image.shape) != 3:
            return True
        width,height,_ = image.shape
        (f_width,f_height) = filter_size
        if width<f_width and height<f_height:
            return True
    else:
        return False

def dir_traverse(rootDir):
    count = 0
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            # print(os.path.join(root, d))
            pass

        for f in files:
            filepath = os.path.join(root, f)
            # print(filepath)
            # print('\n')

            if filter(filepath,'.jpg',(300,300)):
                count=count+1
                print(filepath)
                os.remove(filepath)
    print('the total filterrd image number is: '+ str(count))



dir_traverse(r'./')
