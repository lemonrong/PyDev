from PIL import Image
from numpy import *
from pylab import *
import imtools

im = array(Image.open('PolarBear.jpg').convert('L'))
im2 = 255 - im

im3 = (100.0/ 255 ) * im + 100 # 灰度100-200区间
im4 = 255.0*(im/255.0)**2

print(int(im.min()), int(im.max()))
print(int(im2.min()), int(im2.max()))
print(int(im3.min()), int(im3.max()))
print(int(im4.min()), int(im4.max()))

# im5, cdf = imtools.histeq(im);

imshow(im5)
show()
