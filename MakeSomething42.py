import numpy as np
from PIL import Image, ImageDraw

string = input()

Image_object = Image.new(mode= "RGB", size=(6 * len(string), 15))

Im = ImageDraw.Draw(Image_object)
Im.text((0, 0), string, fill=(255, 255, 255))

ImageNumpy = np.asarray(Image_object)
for row in ImageNumpy:
    for cell in row:
        print("42" if cell[0] > 90 else "  ", end="")
    print("")
