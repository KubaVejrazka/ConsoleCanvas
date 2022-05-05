# This is the main project file.

from ImageGenerator import ImageGenerator
from PIL import Image, ImageOps
from pathlib import Path


class Main:

    # specify current working directory:
    cwd = str(Path(__file__).parent.absolute())

    # specify maximum width & length:
    maxSize = (150, 150)

    try:
        # open image:
        imgPath = cwd + "/image.jpg"
        img = Image.open(imgPath)

        imgTemp = img

        img.thumbnail(maxSize, Image.ANTIALIAS)
        img = ImageOps.exif_transpose(imgTemp)

        # delete unnecessary var to free some memory:
        del imgTemp

        imgC = img.load()

        # start ImageGenerator.GetTxt with selected image:
        ImageGenerator.GetTxt(img.width, img.height, imgC)

    # print error message in case "image.jpg" doesn't exist:
    except IOError:
        print("ERROR: image not found")
