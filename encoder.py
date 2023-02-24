from PIL import Image
import math
import os

def file_to_bitstring(filename):
    with open(filename, "rb") as file:
        byte = file.read(1)
        bit_string = ""
        while byte:
            bits = bin(byte[0])[2:].rjust(8, "0")
            bit_string += bits
            byte = file.read(1)
    return bit_string

# Read file and convert to bit string

input_filename = "elo.txt"
output_folder = "./output"
bit_string = file_to_bitstring(input_filename)
bitstring_filename = os.path.join(output_folder, "bits.txt")

# Save bit string to file
with open(bitstring_filename, "w") as file:
    file.write(bit_string)

# Read bit string from file and rebuild original file
with open(bitstring_filename, "r") as file:
    bit_string = file.read()

root = math.ceil(math.sqrt(len(bit_string)))

width = root 
height = root

image_data = []
for i in range(len(bit_string)):
    if bit_string[i] == "0":
        image_data.append((0, 0, 0))  # black pixel
    else:
        image_data.append((255, 255, 255))  # white pixel

# add a red pixel at the end of the image to indicate the end of the bit string
image_data.append((255, 0, 0))

image = Image.new("RGB", (width, height))  # increase the height by 1 for the red pixel
image.putdata(image_data)
image.show()
