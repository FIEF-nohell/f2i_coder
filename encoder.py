# imports
from PIL import Image
import bitstring
import time
import math
import sys
import os

# get the file information 
input_folder = "./input/"
output_folder = "./encoded/"
filename = os.listdir(input_folder)[0]
filetype = os.path.splitext(filename)[1]

 
# multiplier for the color brightness
pixel_color_multiplier = 255

bitstring = bitstring.BitArray(filename=input_folder + filename).bin

# calculate the image dimensions
extension_bitstring = ''.join(format(ord(c), '08b') for c in filetype)
root = math.ceil(math.sqrt(len(bitstring)+len(extension_bitstring)))
width = root 
height = root

# create the image, display it and save it
image_data = []
counter = 1
total = root*root
t1 = time.time()
print("\n\n---- Printing " + str(root) + "x" + str(root) + " grid | " + str(total)+ " pixels total ----\n")

start_time = time.time()  # record the start time
num_iterations = len(bitstring)

for i in range(num_iterations):
    if i % root == 0 and i != 0: 
        elapsed_time = time.time() - start_time
        remaining_time = 0
        pixels_per_second = 0
        if elapsed_time > 0:
            remaining_time = elapsed_time * (num_iterations - i) / i
            pixels_per_second = i / elapsed_time
        print(f"printing {((i / num_iterations) * 100):.2f}% done | about {remaining_time:.2f} seconds remaining | {pixels_per_second:.2f} pixels/second", end='\r')
    if bitstring[i] == "0":
        image_data.append((0, 0, 0))  # black pixel
    else:
        image_data.append((1*pixel_color_multiplier, 1*pixel_color_multiplier, 1*pixel_color_multiplier))  # slightly lighter pixel
t2 = round(time.time() - t1,2)
print(f"\n\nImage printing took {t2} seconds\n")

# add a different pixel at the end of the image to indicate the end of the bit string
image_data.append((169, 0, 0))

for i in range(len(extension_bitstring)):
    if extension_bitstring[i] == "0":
        image_data.append((0, 0, 0))  # black pixel
    else:
        image_data.append((1*pixel_color_multiplier, 1*pixel_color_multiplier, 1*pixel_color_multiplier))  # slightly lighter pixel

print("Creating image file...\n")
t1 = time.time()
# add a different pixel at the end of the image to indicate the end of the bit string
image_data.append((169, 00, 00))
image = Image.new("RGB", (width, height))
image.putdata(image_data)
image.save(output_folder + "encoded.png")
#image.show()
t2 = round(time.time() - t1,2)
print(f"Image file created in {t2} seconds\n")
print(f"---- Done! ----")