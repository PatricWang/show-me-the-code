from PIL import Image
import os

img_path = r"pics"
for root, dirs, files in os.walk(img_path):
    for f in files:
        img = Image.open(os.path.join(root,f))
        img = img.resize([64,100]).save(os.path.join(root,'rs_' + f),'jpeg')