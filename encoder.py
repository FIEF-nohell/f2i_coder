from PIL import Image
import bitstring
import math
import os

filename = "input.mp4"
filetype = os.path.splitext(filename)[1]
output_filename = "./output/" + f"output{filetype}"

with open(filename, "rb") as file:
    binary_data = file.read()

bitstring = bitstring.BitArray(filename=filename).bin

# calculate the image dimensions
root = math.ceil(math.sqrt(len(bitstring)))
width = root 
height = root+1
# ---------------------------------------

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
        image_data.append((255, 255, 255))  # white pixel

# add a red pixel at the end of the image to indicate the end of the bit string
image_data.append((169, 00, 00))

extension_bitstring = ''.join(format(ord(c), '08b') for c in filetype)

for i in range(len(extension_bitstring)):
    if i % root == 0: 
        print("row done: " + str(counter) + "/" + str(root) + " | " + str(root*counter) + "/" + str(total)+ " pixels")
        counter += 1
    if extension_bitstring[i] == "0":
        image_data.append((0, 0, 0))  # black pixel
    else:
        image_data.append((255, 255, 255))  # white pixel

# add a red pixel at the end of the image to indicate the end of the bit string
image_data.append((169, 00, 00))

image = Image.new("RGB", (width, height))
image.putdata(image_data)
image.save("./output/output.png")
image.show()
# ---------------------------------------