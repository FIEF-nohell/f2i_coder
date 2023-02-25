from PIL import Image
import bitstring as bs
import math

# get the file information 
input_folder = "./encoded/"
output_folder = "./decoded/"
filename = "encoded.png"

# load the image and get the pixels
image = Image.open(input_folder + filename)
pix = image.load()
image_dimensions = image.size[0]
colorset = [255, 169, 0]
print("image dimensions: " + str(image_dimensions) + "x" + str(image_dimensions))  # Get the width and hight of the image for iterating over

bitstring = bs.BitArray(filename=input_folder + filename).bin
print(bitstring)

""" for x in range(image_dimensions):
    for y in range(image_dimensions):


with open("decoded" + chr(int(current_string[1][:8], 2)), "wb") as file:
    file.write(current_string[0])  """