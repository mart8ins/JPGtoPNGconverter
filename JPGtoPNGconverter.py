import sys
import os
from PIL import Image


JPGLocation = sys.argv[1] # lokācija jpg failiem
PNGLocation = sys.argv[2] # jaunā lokācija, kur radīt folderi png

# store image lists
JPGImages = os.listdir(f"./{JPGLocation}")
PNGImages = []

# check if folder where to store PNG exists. Create it or get existing images
if os.path.exists(f"./{PNGLocation}"):
    PNGImages = os.listdir(f"./{PNGLocation}")
else: 
    os.mkdir(PNGLocation) # create directory for png images

# convert JPG images to PNG images
for img in JPGImages:
    jpg_name = img[:-4]
    png_image_exists = False
    for pngImage in PNGImages:
        png_name = pngImage[:-4]
        if jpg_name == png_name:
            png_image_exists = True
            break
    if not png_image_exists:
        jpg_img = Image.open(f"./{JPGLocation}/{img}")
        jpg_img.save(f"{PNGLocation}{jpg_name}.png", "png")
        print(f"Image {jpg_name} converted")
    png_image_exists = False


    
