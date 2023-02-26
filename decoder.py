from PIL import Image
import bitstring as bs
import time
import math
import os

# get the file information 
input_folder = "./encoded/"
output_folder = "./decoded/"
filename = os.listdir(input_folder)[0]

# load the image and get the pixels
image = Image.open(input_folder + filename)
pix = image.load()
image_dimensions = image.size[0]
colorset = [255, 169, 0]
print("image dimensions: " + str(image_dimensions) + "x" + str(image_dimensions))  # Get the width and hight of the image for iterating over

# iterate over each pixel and read its binary data
separator_counter = 0
binary_data = bs.BitArray().bin
binary_data_ext = bs.BitArray().bin
for y in range(image_dimensions):
    for x in range(image_dimensions):
        if pix[x,y][0] == 169:
            separator_counter += 1
            if separator_counter == 2: break
        if pix[x,y][0] == 0:
            if separator_counter == 0: binary_data += "0"
            elif separator_counter == 1: binary_data_ext += "0"
        if pix[x,y][0] == 255:
            if separator_counter == 0: binary_data += "1"
            elif separator_counter == 1: binary_data_ext += "1"
    if separator_counter == 2: break


print(binary_data[:40])
binary_data_bits = int(binary_data, 2)
binary_data_ext_bits = int(binary_data_ext, 2)
# convert the integer into a byte-like object
byte_string = binary_data_bits.to_bytes((binary_data_bits.bit_length() + 7) // 8, 'big')
byte_string_ext = binary_data_ext_bits.to_bytes((binary_data_ext_bits.bit_length() + 7) // 8, 'big')
    
with open(output_folder + "decoded"+byte_string_ext.decode("utf-8"), "wb") as file:
    file.write(byte_string) 

print("Done!")