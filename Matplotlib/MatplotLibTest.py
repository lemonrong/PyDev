from PIL import Image
from pylab import *

im = array(Image.open('PolarBear.jpg'))
imshow(im)

// 在python窗口中可以实现。
#print('Please click 3 points')
#x = ginput(3)
#print('You clicked:', x)

x = [100,100,400,400]
y = [200,500,200,500]

plot(x,y,'r*')

plot(x[:2], y[:2])

title('Plotting:"PolarBear.jpg"')
axis('off')

show()