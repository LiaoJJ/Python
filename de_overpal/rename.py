# -*- coding: utf-8 -*-
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import hashlib
import os
import shutil
import cp2adir
import de_overlap

'''
把 dir 目录下的所有.jpg文件按照 0.jpg, 1.jpg, ..., n.jpg 重命名， 并删除所有非 .jpg 格式的文件 
'''

def rename(dir):
    filelist = os.listdir(dir)
    for i,file in enumerate(filelist):
        oldfilepath = os.path.join(dir,file)
        newfilepath = os.path.join(dir,str(i) + '.jpg')
        if os.path.isfile(oldfilepath):
            if os.path.splitext(oldfilepath)[1] == '.jpg':
                os.rename(oldfilepath,newfilepath)
            else:
                os.remove(oldfilepath)
