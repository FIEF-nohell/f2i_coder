# imports
from PIL import Image
import bitstring
import math
import os

# get the file information 
input_folder = "./input/"
output_folder = "./encoded/"
filename = "alla.docx"
filetype = os.path.splitext(filename)[1]
 
# multiplier for the color brightness
pixel_color_multiplier = 255

bitstring = bitstring.BitArray(filename=input_folder + filename).bin

# calculate the image dimensions
root = math.ceil(math.sqrt(len(bitstring)))
width = root 
height = root+1

# create the image, display it and save it
image_data = []
counter = 1
total = root*root
for i in range(len(bitstring)):
    if i % root == 0: 
        print("row done: " + str(counter) + "/" + str(root) + " | " + str(root*counter) + "/" + str(total)+ " pixels")
        counter += 1
    if bitstring[i] == "0":
        image_data.append((0, 0, 0))  # black pixel
    else:
        image_data.append((1*pixel_color_multiplier, 1*pixel_color_multiplier, 1*pixel_color_multiplier))  # slightly lighter pixel

# add a different pixel at the end of the image to indicate the end of the bit string
image_data.append((1*pixel_color_multiplier, 0, 0))

extension_bitstring = ''.join(format(ord(c), '08b') for c in filetype)

for i in range(len(extension_bitstring)):
    if i % root == 0: 
        print("row done: " + str(counter) + "/" + str(root) + " | " + str(root*counter) + "/" + str(total)+ " pixels")
        counter += 1
    if extension_bitstring[i] == "0":
        image_data.append((0, 0, 0))  # black pixel
    else:
        image_data.append((1*pixel_color_multiplier, 1*pixel_color_multiplier, 1*pixel_color_multiplier))  # slightly lighter pixel

# add a different pixel at the end of the image to indicate the end of the bit string
image_data.append((1*pixel_color_multiplier, 00, 00))

image = Image.new("RGB", (width, height))
image.putdata(image_data)
image.save(output_folder + "encoded.png")
image.show()