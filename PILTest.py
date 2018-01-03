from PIL import Image
import os


pil_im = Image.open('PolarBear.JPG')
pil_gray = pil_im.convert('L')
pil_gray.save('PolarBear_Gray.JPG')

pil_thumbnail = pil_im.copy()
pil_thumbnail.thumbnail((128,128))
pil_thumbnail.save('PolarBear_thumbnail.jpg')

box = (100,100,400,400)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_crop = pil_im.copy()
pil_crop.paste(region, box)
pil_crop.save('PolarBear_Crop.jpg')


pil_resize = pil_im.resize((128,128))
pil_resize.save('PolarBear_Resize.jpg')

pil_rotate = pil_im.rotate(45)
pil_rotate.save('PolarBear_Rotate.jpg')