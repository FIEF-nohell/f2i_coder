from PIL import Image
import bitstring as bs
import math
import os

# get the file information 
input_folder = "./encoded/"
output_folder = "./decoded/"
filename = os.listdir(input_folder)[0]
print(os.listdir(input_folder))

# load the image and get the pixels
image = Image.open(input_folder + filename)
pix = image.load()
image_dimensions = image.size[0]
colorset = [255, 169, 0]
print("image dimensions: " + str(image_dimensions) + "x" + str(image_dimensions))  # Get the width and hight of the image for iterating over

# iterate over each pixel and read its binary data
separator_counter = 0
binary_data = bytearray()
binary_data = bytearray()
for x in range(image_dimensions):
    for y in range(image_dimensions):
        if pix[x,y][0] == 169:
            separator_counter += 1
            binary_data.append(0)

        if pix[x,y][0] == 0:
            if separator_counter == 0: binary_data.append(0)
            if separator_counter == 1: binary_data.append(0)
        if pix[x,y][0] == 255:
            binary_data.append(1)

"""
with open("decoded" + chr(int(current_string[1][:8], 2)), "wb") as file:
    file.write(current_string[0])  """