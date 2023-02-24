from PIL import Image
import bitstring
import math
import os

filename = "alla.png"
output_filename = "./output/" + f"output{filetype}"

with open(filename, "rb") as file:
    binary_data = file.read()

bitstring = bitstring.BitArray(filename=filename).bin

with open(output_filename, "wb") as file:
    file.write(binary_data)

