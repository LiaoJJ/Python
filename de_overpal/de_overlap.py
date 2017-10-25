# -*- coding: utf-8 -*-
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import hashlib
import os
import shutil

'''
把 ori_data_path 中的所有文件通过 hash 法去重，
去重后的图片存储在 new_data_path 中
'''

ori_data_path = r'./data'
new_data_path = r'./newdata'

# data0 =mpimg.imread('data/0.jpg')
# data0d = mpimg.imread('data/0.jpg')
# print(data0.shape)

# plt.imshow(data0)
# plt.show()
#
# img = plt.imshow(data0[:,:,0])
# img.set_cmap('gray')
# plt.show('data0')

# lena_new_sz = misc.imresize(data0, 0.5) # 第二个参数如果是整数，则为百分比，如果是tuple，则为输出图像的尺寸
# plt.imshow(lena_new_sz)
# plt.axis('off')
# print(lena_new_sz.shape)
# plt.show()

# misc.imsave('lena_new_sz.jpg', lena_new_sz)

# print(hashlib.md5(data0).hexdigest())
# print(hashlib.md5(data0d).hexdigest())

# os.remove('./data/1 - 副本.jpg')

# pichash = np.array(np.zeros([len(os.listdir('./')),2]))

pichash = {}
for filename in os.listdir(ori_data_path):
    # data0 = mpimg.imread(ori_data_path+'/'+filename)
    with open(ori_data_path+'/'+filename,'rb') as f:
        pichash[hashlib.md5(f.read()).hexdigest()] = filename
print(pichash)

if not os.path.exists(new_data_path):
    os.mkdir(new_data_path)
for pic in pichash.values():
    shutil.copy(ori_data_path+'/'+pic,new_data_path+'/'+pic)

print('end')
# picname = os.listdir(r'./')
