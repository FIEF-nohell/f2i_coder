# imports
from tqdm import tqdm
from PIL import Image
import bitstring
import time
import math
import os

# get the file information 
input_folder = "./input/"
output_folder = "./encoded/"
filename = os.listdir(input_folder)[0]
filetype = os.path.splitext(filename)[1]

bitstring = bitstring.BitArray(filename=input_folder + filename).bin

# calculate the image dimensions
extension_bitstring = ''.join(format(ord(c), '08b') for c in filetype)
root = math.ceil(math.sqrt(len(bitstring)+len(extension_bitstring)))
width = root 
height = root

# create the image, display it and save it
image_data = []
total = root*root

print("\n---- Printing " + str(root) + "x" + str(root) + " grid | " + str(total)+ " pixels total ----")

start_time = time.time()  # record the start time
num_iterations = len(bitstring)

for i in tqdm(range(num_iterations), desc="Processing Image"):
    if bitstring[i] == "0":
        image_data.append((0, 0, 0))  # black pixel
    else:
        image_data.append((255, 255, 255))

# add a different pixel at the end of the image to indicate the end of the bit string
image_data.append((169, 0, 0))

for i in range(len(extension_bitstring)):
    if extension_bitstring[i] == "0":
        image_data.append((0, 0, 0))  # black pixel
    else:
        image_data.append((255, 255, 255))

print("\nCreating image file...")
t1 = time.time()
# add a different pixel at the end of the image to indicate the end of the bit string
image_data.append((169, 00, 00))
image = Image.new("RGB", (width, height))
image.putdata(image_data)
image.save(output_folder + "encoded.png")
t2 = round(time.time() - t1,2)

print(f"Image file created in {t2} seconds\n")
print(f"---- Done! ----\n")