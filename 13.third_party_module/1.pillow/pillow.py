
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

im = Image.open('2019_8_25.jpg')

w, h = im.size

print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))

# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

from PIL import Image,ImageDraw,ImageFont, ImageFilter

import random

def rndChar():
    return chr(random.randint(65,90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60

font_fullpath = r'C:\Windows\Fonts\Arial.ttf'

image = Image.new('RGB', (width,height), (255,255,255))

font = ImageFont.truetype(font_fullpath, 36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x,y), fill = rndColor())

for t in range(4):
    draw.text((60*t + 10, 10), rndChar(), font=font, fill=rndColor2())
    
#image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
        