# ConsoleCanvas
Allows user to draw an image using ASCII characters.

## How to install:
1) Clone ConsoleCanvas:
```
git clone https://github.com/KubaVejrazka/ConsoleCanvas.git
```
2) Install Pillow:
```
pip install Pillow
```

## How to use:
First, you want to set up your terminal. It's quite simple, you just scroll out as far as you can, so you can fit as much text in the window as possible.
Also, I recommend changing your terminal's font to "Liberation Mono", for equal spaces between columns and rows, so your image isn't disorted.

#### Run with the default charset:
Open your terminal inside /ConsoleCanvas/bin and run:
```
python Start.py
```

#### Run with the PixelArt charset:
Open your terminal inside /ConsoleCanvas/bin and run:
```
python Start.py pixelart
```

#### Run with a custom charset:
First, you should edit your custom charset. You can do that by following the instructions at the end of this README.

Open your terminal inside /ConsoleCanvas/bin and run:
```
python Start.py custom
```

#### Edit the image size:
If you want to edit the image size (for example if the image is too big for your terminal window), you can use this argument:
```
size=<targeted image size, i recommend 100-300>
```

#### Use a custom image:
For opening an image other, than the default one, you can use the following argument:
```
path=<image path>
```

## Edit your custom charset:
1) Open "CustomCharset.py" in your editor.
2) Put each character inside one pair of single quotes.
3) Save the file.
