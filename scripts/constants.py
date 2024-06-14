from scripts.encoders.huffman import Huffman
from scripts.encoders.block import Block
import string, os

# Get the current directory (from is executed the program, so is main.py folder)

current_directory = os.getcwd()

# Paths

imgs_folder_path = current_directory + "\\imgs"
original_frames_folder_path = current_directory + "\\imgs\\original_frames"
video_frames_imgs_folder_path = current_directory + "\\imgs\\video_frames"
videos_folder_path = current_directory + "\\videos"
logs_text_file_path = current_directory + "\\logs\\log.txt"

# Formats

IMG_FORMATS = ["png", "jpg"]
TXT_FORMATS = ["txt"]

# ASCII printable characters 

ASCII_PRINTABLE_SYMBOLS = string.printable

# Entropy arity

ENTROPY_ARITY = 2

# Universal delimiter

SOURCE_CODE_DELIMITER = "¿"

# Lenght of the block code

BLOCK_CODE_LENGTH = 8

# Number of bits per channel (R, G, B)

BITS_PER_CHANNEL = 8

# List of coding methods

CODING_METHODS = {
    "huffman" : Huffman,
    "block"   : Block,
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