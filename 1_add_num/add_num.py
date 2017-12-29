

from PIL import Image, ImageDraw, ImageFont
from test_pil import *


def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
    img.save('./pic/result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('./pic/1.jpg')
    add_num(image)
    thumbnail_img(image)
    verifiCode()