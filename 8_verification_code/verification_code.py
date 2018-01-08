import string,random
from PIL import Image,ImageFont,ImageFilter,ImageDraw

def get_random_color():
    return tuple([random.randint(50,150) for _ in range(3)])

def get_verify_picture():
    font_path = "c:/Windows/fonts/SIMHEI.ttf"
    letters = [random.choice(string.letters) for i in range(4)]
    font = ImageFont.truetype(font_path,50)
    width,height = 240,60
    pic = Image.new('RGB',(width,height),(200,200,200))
    draw = ImageDraw.Draw(pic)

    for i in range(width):
        for j in range(height):
            draw.point((i,j),fill = get_random_color())

    for i,letter in enumerate(letters):
        draw.text((60*i + random.randrange(0,20),random.randrange(0,10)),letter,font = font,fill = get_random_color())
    # for i in range(5000):
    #     draw.point((random.randint(0,width),random.randint(0,height)),fill = get_random_color())

    pic.filter(ImageFilter.BLUR)
    pic.save('1.jpg','jpeg')

get_verify_picture()