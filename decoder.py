# imports
import bitstring as bs
from PIL import Image
from tqdm import tqdm
import numpy as np
import time
import os

# get the file information 
input_folder = "./encoded/"
output_folder = "./decoded/"
filename = os.listdir(input_folder)[0]

# load the image and get the pixels
image = Image.open(input_folder + filename)
#pix = image.load()
image_dimensions = image.size[0]
#colorset = [255, 169, 0]
print("\n\n---- Image dimensions: " + str(image_dimensions) + "x" + str(image_dimensions) + " ----\n")

# Convert the image to a NumPy array
pixel_array = np.array(image)

# Reshape the pixel array to a 2D array of shape (num_pixels, 3)
num_pixels = pixel_array.shape[0] * pixel_array.shape[1]
pixel_array = pixel_array.reshape(num_pixels, 3)

# Extract the red values into array
r_values = pixel_array[:, 0]
r_values[r_values == 255] = 1

# Find the index of the number 169 in the array
index = np.where(r_values == 169)[0][0]

binary_data = r_values[0:index]
binary_data_ext = r_values[index+1:]

index2 = np.where(binary_data_ext == 169)[0][0]
binary_data_ext = binary_data_ext[:index2]

print(f"Converting into bytes...\n")
t1 = time.time()

# Convert the array to a string representing a file extension
extension = ''.join([chr(int(''.join(map(str, binary_data_ext[i:i+8])), 2)) for i in range(0, len(binary_data_ext), 8)])

result = bytearray(binary_data)
print(result)

t2 = round(time.time() - t1, 2)
print(f"Converting binary format took {t2} seconds\n")

t1 = time.time()
with open(output_folder + "decoded" + extension, "wb") as file:
    file.write(result) 
t2 = round(time.time() - t1, 2)

print(f"Created output file in {t2} seconds\n")
print("---- Done! ----")