import os

import PIL
from PIL import Image

def scale(image, scaling):
    name = os.path.basename(image)
    name = os.path.splitext(name)

    try:
        im = Image.open(f'sprites/scaled/{name[0]}_x{scaling}{name[1]})')

    except:
        im = Image.open(image)
        w, h = im.width * scaling, im.height * scaling
        im = im.resize((w, h), Image.NEAREST)
        im.save(f'sprites/scaled/{name[0]}_x{scaling}{name[1]}')

    return f'sprites/scaled/{name[0]}_x{scaling}{name[1]}'

def flip_horizontal(image):
    im = Image.open(image)
    name = os.path.basename(image)
    name = os.path.splitext(name)

    im = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    im.save(f'sprites/flipped/{name[0]}_horizontal{name[1]}')

    return f'sprites/flipped/{name[0]}_horizontal{name[1]}'

def flip_vertical(image):
    im = Image.open(image)
    name = os.path.basename(image)
    name = os.path.splitext(name)

    im = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    im.save(f'sprites/flipped/{name[0]}_vertical{name[1]}')

    return f'sprites/flipped/{name[0]}_vertical{name[1]}'
