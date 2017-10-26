# -*- coding: utf-8 -*-
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import hashlib
import os
import shutil

'''
把 './' 下的所有文件夹内的所有文件，移动到'./data'，并重命名为'原文件夹名'+'文件名'
'''

def cpdirs2adir(topath):
    def coverFiles(sourceDir, targetDir):
        for file in os.listdir(sourceDir):
            sourceFile = os.path.join(sourceDir, file)
            targetFile = os.path.join(targetDir, sourceDir + file)
            # cover the files
            if os.path.isfile(sourceFile):
                shutil.copyfile(sourceFile,targetFile)

    highpath = r'./'
    # topath = r'./data'
    if not os.path.exists(topath):
        os.mkdir(topath)

    for dir in os.listdir(highpath):
        if os.path.isdir(dir):
            coverFiles(dir,topath)