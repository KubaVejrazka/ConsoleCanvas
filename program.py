# This is the main project file.

from PIL import Image

imgPath = "image.png"
global img;

try:
    img = Image.open(imgPath)
    width = img.width
    height = img.height
    print(width, height)

except IOError:
    print("hehe")
    pass