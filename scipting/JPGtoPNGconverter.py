"""
jpg to png converter
"""

import sys
import os
from PIL import Image

# import shutil #not needed since the same file name is not generated again so you wont need to delete the generated folder


# grab first and second arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder, output_folder)

# check is new/ exists, if not create
# if os.path.exists(output_folder):
#     shutil.rmtree(output_folder)  #rmtree deletes an unempty dir

if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # creates a new folder

# loop thru pokedex
for filename in os.listdir(image_folder):
    # img = Image.open(f"{image_folder}{filename}") #same result with the code below
    img = Image.open(os.path.join(image_folder, filename))
    clean_name = os.path.splitext(filename)[
        0
    ]  # splits the text into a  tuple, eg ('pikachu','.jpg')
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("all done")
# convert images to png
