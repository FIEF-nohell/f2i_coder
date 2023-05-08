# imports
from PIL import Image
import bitstring as bs
import math
import os
import threading

# get the file information
input_folder = "./input/"
output_folder = "./encoded/"
filename = os.listdir(input_folder)[0]
filetype = os.path.splitext(filename)[1]

bitstring = bs.BitArray(filename=input_folder + filename).bin

# calculate the image dimensions
extension_bitstring = ''.join(format(ord(c), '08b') for c in filetype)
root = math.ceil(math.sqrt(len(bitstring)+len(extension_bitstring)))
width = root
height = root

# create the image
image_data = [None] * len(bitstring)
total = root * root

print(f"\n---- Printing {root}x{root} grid | {total} pixels total ----\n")

num_iterations = len(bitstring)

# function to process a range of bits
def process_bits(bitstring, start, end, image_data):
    for i in range(start, end):
        if bitstring[i] == "0":
            image_data[i] = (0, 0, 0)  # black pixel
        else:
            image_data[i] = (255, 255, 255)

# create four threads and assign equal work to each
# 16 / 16,2
# 8 / 16,13
num_threads = 8
chunk_size = num_iterations // num_threads
threads = []

for i in range(num_threads):
    start = i * chunk_size
    end = (i+1) * chunk_size if i != num_threads - 1 else num_iterations
    thread = threading.Thread(target=process_bits, args=(bitstring, start, end, image_data))
    thread.start()
    threads.append(thread)

# wait for all threads to finish
for thread in threads:
    thread.join()

image = Image.new("RGB", (width, height))
image.putdata(image_data)
image.save(output_folder + "encoded_mt.png")

print(f"---- Image created ----\n")