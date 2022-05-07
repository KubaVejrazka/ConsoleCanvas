# This is the main project file.

import sys
import pwd
import os
from ImageGenerator import ImageGenerator
from PIL import Image, ImageOps
from pathlib import Path


class Main:

    # specify current working directory:
    cwd = str(Path(__file__).parent.parent.absolute())

    # specify maximum width & length:
    maxSize = (150, 150)

    try:
        customPath = ""
        pixelArt = False
        custom = False

        # go through arguments:
        for x in range(1, len(sys.argv)):
            arg = str(sys.argv[x])

            if "path=" in arg:
                arg = arg[5:]
                customPath = arg
                 

            elif arg == "pixelart": pixelArt = True
            elif arg == "custom": custom = True

        # open image:
        if customPath != "": imgPath = "/home/" + pwd.getpwuid(os.geteuid())[0] + customPath
        else: imgPath = cwd + "/image.jpg"
        print(imgPath)

        img = Image.open(imgPath)

        imgTemp = img

        img.thumbnail(maxSize, Image.ANTIALIAS)
        img = ImageOps.exif_transpose(imgTemp)
        imgC = img.load()

        # delete unnecessary var to free some memory:
        del imgTemp

        # start ImageGenerator.GetTxt with selected image:
        ImageGenerator.GetTxt(img.width, img.height, imgC, pixelArt, custom)

    # print error message in case "image.jpg" doesn't exist:
    except IOError:
        print("ERROR: image not found")