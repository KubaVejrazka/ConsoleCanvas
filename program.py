# This is the main project file.

from tkinter import Image

global img;

try:
    img = Image.open("image.png")


except IOError:
    pass