from PIL import Image
import bitstring
import math
import os

# get the file information 
input_folder = "./encoded/"
output_folder = "./decoded/"
filename = "encoded.png"

with open(input_folder + filename, "rb") as file:
    binary_data = file.read()

bitstring = bitstring.BitArray(filename=filename).bin

with open(output_filename, "wb") as file:
    file.write(binary_data)

