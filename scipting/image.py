"""
This module provides functionalities for [describe the purpose of the module].

"""

from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img .filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')
filtered_img.save("grey.png","png")
filtered_img.show()

# .format, .size , .rotate , .resize
img.thumbnail((400,400)) #resize the image 
