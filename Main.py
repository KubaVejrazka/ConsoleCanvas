# This is the main project file.
from ImageGenerator import ImageGenerator
from PIL import Image
from pathlib import Path


class Main:

    # specifying path to image
    cwd = str(Path(__file__).parent.absolute())

    global img

    try:

        imgPath = cwd + "/image.jpg"
        print(imgPath)

        img = Image.open(imgPath)
        imgC = img.load()

        ImageGenerator.GetTxt(img.width, img.height, imgC)

    # in case "image.jpg" doesn't exist:
    except IOError:
        print("ERROR: image not found")
