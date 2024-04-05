from huffman import Huffman
import string

# ASCII printable characters 

ASCII = string.printable

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

# Youtube resolutions

RESOLUTIONS = {
    426*240 : [426, 240],
    640*360 : [640, 360],
    854*480 : [854, 480],
    1280*720 : [1280, 720],
    1920*1080 : [1920, 1080],
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