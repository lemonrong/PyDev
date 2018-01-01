from PIL import Image
import os


pil_im = Image.open('PolarBear.JPG')
pil_gray = pil_im.convert('L')
pil_gray.save('PolarBear_Gray.JPG')

pil_thumbnail = pil_im.thumbnail((128,128))

box = (100,100,400,400)
region = pil_im.crop(box)
region = region.traspose(Image.ROTATE_180)
pil_im.paste(region, box)