# imports
from PIL import Image
import bitstring
import threading
import time
import math
import sys
import os

print(f"\n\n##### FILE TO IMAGE CONVERTER by nohell #####\n")

# get the file information 
didnt_exist = False
input_folder = "./input/"
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    didnt_exist = True

output_folder = "./encoded/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    didnt_exist = True

if didnt_exist: 
    print("\nSome needed folders were not created yet. Please relaunch the script.\n")    
    sys.exit()
print(f"\nLoading file to memory. Depending on the file size this can take a while.\n")
try:
    filename = os.listdir(input_folder)[0]
except:
    print(f"\nNo input file found. Please relaunch the script with a file in the {input_folder} folder.\n")
    sys.exit()
filetype = os.path.splitext(filename)[1]
file_size = os.path.getsize(input_folder+filename) / (1024 * 1024)

bitstring = bitstring.BitArray(filename=input_folder + filename).bin

# calculate the image dimensions
extension_bitstring = ''.join(format(ord(c), '08b') for c in filename)
root = math.ceil(math.sqrt(len(bitstring)+len(extension_bitstring)))
width, height = root, root
image_data = [None] * len(bitstring)
total_pixels = height*width

print(f"\n---- Calculating {root}x{root} image with {total_pixels} pixels | Input size: {file_size:.2f} MB | Estimated output size: {file_size * 2.2:.2f} MB ----\n")
# record the start time
start_time = time.time() 
num_iterations = len(bitstring)

# function to process a range of bits
def process_bits(bitstring, start, end, image_data, thread_index):
    for i in range(start, end):
        if bitstring[i] == "0":
            image_data[i] = (0, 0, 0)  # black pixel
        else:
            image_data[i] = (255, 255, 255)
    end_time = time.time() - start_time
    print(f"Thread finished. {end_time:.2f} seconds elapsed. (Thread ID: {thread_index})", end="\r")

# create four threads and assign equal work to each
num_threads = 32
chunk_size = num_iterations // num_threads
threads = []

print(f"Launching {num_threads} threads.")

for i in range(num_threads):
    start = i * chunk_size
    end = (i+1) * chunk_size if i != num_threads - 1 else num_iterations
    thread = threading.Thread(target=process_bits, args=(bitstring, start, end, image_data, i))
    thread.start()
    threads.append(thread)

# wait for all threads to finish
for thread in threads:
    thread.join()

# add a different pixel at the end of the image to indicate the end of the bit string
image_data.append((169, 0, 0))

for i in range(len(extension_bitstring)):
    if extension_bitstring[i] == "0":
        image_data.append((0, 0, 0)) 
    else:
        image_data.append((255, 255, 255))

# add a different pixel at the end of the image to indicate the end of the bit string
image_data.append((169, 00, 00))

t1 = time.time()

image = Image.new("RGB", (width, height))
print("\nWriting data to image.")
image.putdata(image_data)

print("Saving image.")
image_format = "png"
output_filename = output_folder + "encoded." + image_format.lower()
image.save(output_filename, format=image_format)

t2 = round(time.time() - t1, 2)

image_size = os.path.getsize(output_filename) / (1024 * 1024)
ratio = image_size / file_size * 100

print(f"\n---- Image created in {t2} seconds | Output file size: {image_size:.4f} MB (+{ratio:.2f}%) ----\n")