from huffman import Huffman

# LIST OF CODING METHODS

CODING_METHODS = {
    "huffman": Huffman,
}

# YOUTUBE RESOLUTIONS

RESOLUTIONS = {
    426*240 : [426, 240],
    640*360 : [640, 360],
    854*480 : [854, 480],
    1280*720 : [1280, 720],
    1920*1080 : [1920, 1080],
}

# BIT DEPTH

BIT_DEPTH = 24

# MODES FOR THE CREATION OF THE IMAGE

MODES = {
    1 : "1",    # Black and white
    8 : "L",    # Grayscale
    24 : "RGB", # Red-Green-Blue
    32 : "RGBA", # Red-Green-Blue-Transparency
}