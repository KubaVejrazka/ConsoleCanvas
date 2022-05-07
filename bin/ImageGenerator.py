# This is a file specifically for converting images to ASCII.

from pathlib import Path
import sys
from PIL import Image

# import custom charset:
cwd = str(Path(__file__).parent.parent.absolute())
sys.path.append(cwd)
from CustomCharset import CustomCharset

class ImageGenerator:

    # main def, called in Start.py:
    def GetTxt(xx, yy, img, pixelArt, custom):

        # default charset:
        chars = [' ', '.', '+', 'o', 'O']

        # pixel art charset:
        if pixelArt:
            chars = [' ', '░', '▒', '▓', '█']

        # custom charset:
        elif custom:
            chars = CustomCharset.chars
        
        n = int(255 / len(chars))

        # go through every pixel:
        for y in range(yy):
            for x in range(xx):

                # calculate average opacity ((RED + GREEN + BLUE) / 3):
                opacity = int((img[x, y][0] + img[x, y][1] + img[x, y][2]) / 3)

                # pick character from charset based on pixel's opacity:
                def charIndex():
                    for i in range(len(chars) + 1):
                        if opacity == 0: return 0
                        elif (i * n) >= (255 - (255 % n)): return len(chars) - 1
                        elif opacity <= (i * n):
                            return i - 1

                print(f"{chars[charIndex()]}{chars[charIndex()]}", end="")

            # go to the next line:
            print()
