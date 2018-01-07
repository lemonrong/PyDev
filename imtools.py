import os
from PIL import Image
from numpy import *

def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im, sz):
    """使用PIL对象重新定义图像数组的大小"""
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
    """对灰度图像进行直方图均衡化"""

    #计算图像的直方图
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum() #cumulative distribution function（累积分布函数cdf）
    cdf = 255 * cdf / cdf[-1] #归一化
    #使用累积分布函数的线性插值，