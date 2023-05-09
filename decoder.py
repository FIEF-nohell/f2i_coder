# imports
from PIL import Image
import numpy as np
import time
import sys
import os

print(f"\n\n##### IMAGE TO FILE CONVERTER by nohell #####\n")

# get the file information 
didnt_exist = False
input_folder = "./encoded/"
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    didnt_exist = True

output_folder = "./decoded/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    didnt_exist = True

if didnt_exist: 
    print("\nSome needed folders were not created yet. Please relaunch the script.\n")
    sys.exit()
try:
    test = os.listdir(input_folder)[0]
    files = os.listdir(input_folder)
except:
    print(f"\nNo input file found. Please relaunch the script with a valid encoded file in the {input_folder} folder.\n")
    sys.exit()
for file in files:
    image_size = os.path.getsize(input_folder + file) / (1024 * 1024)
    print(f"\n\nfile: {file}")
    print(f"size: {image_size:.2f} MB")
    # load the image and get the pixels
    Image.MAX_IMAGE_PIXELS = None
    image = Image.open(input_folder + file)
    image_dimensions = image.size[0]
    print(f"\n---- Image dimensions: {image_dimensions}x{image_dimensions} | Size: {image_size:.2f} MB | Estimated output size: {image_size / 2.2:.2f} MB ----\n")

    print(f"Reading file content.")
    # Convert the image to a NumPy array
    pixel_array = np.array(image)

    # Reshape the pixel array to a 2D array of shape (num_pixels, 3)
    num_pixels = pixel_array.shape[0] * pixel_array.shape[1]
    pixel_array = pixel_array.reshape(num_pixels, 3)

    # Extract the red values into array
    r_values = pixel_array[:, 0]

    # Find the index of the number 169 in the array
    index = np.where(r_values == 169)[0][0]

    binary_data = r_values[0:index].astype(np.uint8)
    binary_data_ext = r_values[index+1:]
    binary_data_ext[binary_data_ext == 255] = 1

    index2 = np.where(binary_data_ext == 169)[0][0]
    binary_data_ext = binary_data_ext[:index2]

    print(f"Converting into bytes.")

    # Convert the array to a string representing a file extension
    extension = ''.join([chr(int(''.join(map(str, binary_data_ext[i:i+8])), 2)) for i in range(0, len(binary_data_ext), 8)])

    result = bytes(np.packbits(binary_data))

    print(f"Creating file '{extension}'.\n")
    t1 = time.time()
    with open(output_folder + extension, "wb") as file:
        file.write(result) 
    t2 = round(time.time() - t1, 2)

    print(f"---- Created output file in {t2:.2f} seconds ----\n")