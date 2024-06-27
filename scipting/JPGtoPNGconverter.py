"""
jpg to png converter
"""

import sys
import os
from PIL import Image


# grab first and second arg
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder, output_folder)

# check is new/ exists, if not create
print(os.path.exists(output_folder))
# loop thru pokedex
# convert images to png
