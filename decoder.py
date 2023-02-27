from PIL import Image
import bitstring as bs
import binascii
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
print("reading file...\n")

# iterate over each pixel and read its binary data
separator_counter = 0
binary_data = bytearray()
binary_data_ext = bs.BitArray().bin
t1 = time.time()
for y in range(image_dimensions):
    print(" reading " + str(((y/(image_dimensions)))*100)[:5] + "% done", end='\r')
    for x in range(image_dimensions):
        if pix[x,y][0] == 169:
            separator_counter += 1
            if separator_counter == 2: break
        if pix[x,y][0] == 0:
            if separator_counter == 0: binary_data.append(0)
            elif separator_counter == 1: binary_data_ext += "0"
        if pix[x,y][0] == 255:
            if separator_counter == 0: binary_data.append(1)
            elif separator_counter == 1: binary_data_ext += "1"
    if separator_counter == 2: break
t2 = time.time() - t1
print(f"file read in {t2} seconds, converting into bytes...\n")

t1 = time.time()
# convert the integer into a byte-like object
binary_data_ext_bits = int(binary_data_ext, 2)
byte_string_ext = binary_data_ext_bits.to_bytes((binary_data_ext_bits.bit_length() + 7) // 8, 'big')

# convert each byte to a binary string and concatenate into a single bitstring
bitstring = ''.join(['{:b}'.format(b) for b in binary_data])
t2 = time.time() - t1
print(f"converting binary format took {t2} seconds\n")

# convert the bitstring to an integer
value = int(bitstring, 2)

# determine the number of bytes needed to represent the integer
num_bytes = (len(bitstring) + 7) // 8

# convert the integer to bytes
result = value.to_bytes(num_bytes, byteorder='big')

t1 = time.time()
with open(output_folder + "decoded"+byte_string_ext.decode("utf-8"), "wb") as file:
    file.write(result) 
t2 = time.time() - t1
print(f"created output file in {t2} seconds")






""" binary_data_bits = int(binary_data, 2)

# determine the number of bytes needed to represent the integer
num_bytes = (binary_data_bits.bit_length() + 7) // 8


# add a leading zero byte if the integer requires an even number of bytes
if num_bytes % 2 == 1:
    num_bytes += 1

# convert the integer into a byte-like object, preserving leading zero bytes
byte_string = binary_data_bits.to_bytes(num_bytes, 'big')
 """