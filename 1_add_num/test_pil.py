# -*- coding:utf-8 -*-
from PIL import Image,ImageFilter,ImageFont,ImageDraw
import random

curPath = './pic/'

def thumbnail_img(im):
    w,h = im.size
    print("img size: %sx%s" % (w,h))
#缩放
    im.thumbnail((w//2,h//2))
    print('resize img to: %sx%s' % (w//2,h//2))
    im.save(curPath + 'thumbnail.jpg','jpeg')
#模糊
    im2 = im.filter(ImageFilter.BLUR)
    im2.save(curPath + 'blurImg.jpg','jpeg')
    return 0

def rndChar():
    return chr(random.randint(65,90))

def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2():
    return(random.randint(32,127),random.randint(32,127),random.randint(32,127))

def verifiCode():
    width = 60 * 4
    height = 60
    img = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf',36)
    draw = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill = rndColor())

    for t in range(4):
        draw.text((60 * t + 10,10),rndChar(),font = font,fill = rndColor2())

    img = img.filter(ImageFilter.BLUR)
    img.save(curPath + 'code.jpg','jpeg')