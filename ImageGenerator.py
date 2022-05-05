# This is a file specifically for converting images to ASCII.

from PIL import Image

class ImageGenerator:

    # main def, called in Start.py
    def GetTxt(xx, yy, img):

        # CHARSET (low to high opacity):
        chars = [' ', '.', '+', 'I', 'W']
        
        # go through every pixel
        for y in range(yy):
            for x in range(xx):

                # calculate average opacity ((RED + GREEN + BLUE) / 3):
                opacity = int((img[x,y][0] + img[x,y][1] + img[x,y][2]) / 3)

                # pick character from CHARSET based on pixel's opacity:
                if opacity <= 0: print("  ", end="")
                if opacity > 0 and opacity <= 51: print(f"{chars[0]}{chars[0]}", end="")
                if opacity > 51 and opacity <= 102: print(f"{chars[1]}{chars[1]}", end="")
                if opacity > 102 and opacity <= 153: print(f"{chars[2]}{chars[2]}", end="")
                if opacity > 153 and opacity <= 204: print(f"{chars[3]}{chars[3]}", end="")
                if opacity > 204: print(f"{chars[4]}{chars[4]}", end="")

            # go to the next line:
            print()
