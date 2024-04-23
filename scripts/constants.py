from scripts.encoders.huffman import Huffman
import string, os

# Get the current directory (from is executed the program, so is main.py folder)

current_directory = os.getcwd()

# Paths

imgs_folder_path = current_directory + "\\imgs"
logs_text_file_path = current_directory + "\\logs\\log.txt"

# ASCII printable characters 

ASCII_PRINTABLE_SYMBOLS = string.printable

# Universal delimiter

SOURCE_CODE_DELIMITER = "~"

# Lenght of the block code

BLOCK_CODE_LENGTH = 8

# Number of bits per channel (R, G, B)

BITS_PER_CHANNEL = 8

# List of coding methods

CODING_METHODS = {
    "huffman": Huffman,
}

# Minimal and maximal resolutions

RESOLUTIONS = {
    "youtube" : [(256, 144), (1920, 1080)],
}

# Bit depth

BIT_DEPTH = 24

# Modes for the creation of images (with PIL)

MODES = {
    1 : "1",    # Black and white
    8 : "L",    # Grayscale
    24 : "RGB", # Red-Green-Blue
    32 : "RGBA", # Red-Green-Blue-Transparency
}