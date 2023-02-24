# Imports
from PIL import Image
import math
import os
# ---------------------------------------



def file_to_bitstring(filename, buffer_size=1024):
    with open(filename, "rb") as file:
        bit_string = ""
        while True:
            buffer = file.read(buffer_size)
            if not buffer:
                break
            for byte in buffer:
                bits = bin(byte)[2:].rjust(8, "0")
                bit_string += bits
    return bit_string


# Define input file and output folder
input_filename = "pp.txt"
output_folder = "./output"

# Read file and convert to bit string
bit_string = file_to_bitstring(input_filename)
bitstring_filename = os.path.join(output_folder, "bits.txt")

# Save bit string to file
with open(bitstring_filename, "w") as file:
    file.write(bit_string)

# calculate the image dimensions
root = math.ceil(math.sqrt(len(bit_string)))
width = root 
height = root
# ---------------------------------------



# create the image, display it and save it
image_data = []
counter = 1
for i in range(len(bit_string)):
    if i % root == 0: 
        print("row done: " + str(counter) + "/" + str(root) )
        counter += 1
    if bit_string[i] == "0":
        image_data.append((0, 0, 0))  # black pixel
    else:
        image_data.append((255, 255, 255))  # white pixel

# add a red pixel at the end of the image to indicate the end of the bit string
image_data.append((100, 142, 169))

image = Image.new("RGB", (width, height))
image.putdata(image_data)
image.save("./output/image.png")
image.show()
# ---------------------------------------