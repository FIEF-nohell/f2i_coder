# imports
from PIL import Image
import bitstring
import threading
import time
import math
import sys
import os

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
filename = os.listdir(input_folder)[0]
filetype = os.path.splitext(filename)[1]
file_size = os.path.getsize(input_folder+filename) / (1024 * 1024)

bitstring = bitstring.BitArray(filename=input_folder + filename).bin

# calculate the image dimensions
extension_bitstring = ''.join(format(ord(c), '08b') for c in filetype)
root = math.ceil(math.sqrt(len(bitstring)+len(extension_bitstring)))
width = root 
height = root

# create the image
image_data = [None] * len(bitstring)
total = root*root

print(f"\n---- Printing {root}x{root} grid | {total} pixels total | input file size {file_size:.4f} MB ----\n")

start_time = time.time()  # record the start time
num_iterations = len(bitstring)

# function to process a range of bits
def process_bits(bitstring, start, end, image_data, thread_index):
    for i in range(start, end):
        if bitstring[i] == "0":
            image_data[i] = (0, 0, 0)  # black pixel
        else:
            image_data[i] = (255, 255, 255)
    print(f"Thread {thread_index} finished processing bits {start} to {end-1}")

# create four threads and assign equal work to each
num_threads = 32
chunk_size = num_iterations // num_threads
threads = []

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

image_size = os.path.getsize(output_folder + "encoded.png") / (1024 * 1024)
ratio = image_size / file_size * 100

print(f"---- Image created in {t2} seconds | Output file size {image_size:.4f} MB (+{ratio:.2f}%) ----\n")