# This is a file specifically for converting images to ASCII.
from os import chdir
from PIL import Image

class ImageGenerator:

    def GetTxt(xx, yy, img):
        for y in range(yy):
            for x in range(xx):
                opacity = int((img[x,y][0] + img[x,y][1] + img[x,y][2]) / 3)
                if opacity <= 0: print("  ", end="")
                if opacity > 0 and opacity <= 51: print("  ", end="")
                if opacity > 51 and opacity <= 102: print("░░", end="")
                if opacity > 102 and opacity <= 153: print("▒▒", end="")
                if opacity > 153 and opacity <= 204: print("▓▓", end="")
                if opacity > 204: print("██", end="")
            print()
