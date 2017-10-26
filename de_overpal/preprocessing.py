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
import rename

'''
把 './' 下的所有文件夹内的所有文件，移动到'./data'，并重命名为'原文件夹名'+'文件名'
'''

topath = r'./data'
ori_data_path = r'./data'
new_data_path = r'./newdata'

cp2adir.cpdirs2adir(topath)
de_overlap.de_overlap(ori_data_path,new_data_path)
shutil.rmtree(ori_data_path)
rename.rename(new_data_path)
