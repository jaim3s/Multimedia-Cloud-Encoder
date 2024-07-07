from scripts.encoders.huffman import Huffman
from scripts.encoders.block import Block
import string, os

# Get the current directory (from is executed the program, so is main.py folder)

current_directory = os.getcwd()

# Paths

content_folder_path = current_directory + "\\content"
logs_text_file_path = current_directory + "\\logs\\log.txt"

# File formats

VIDEO_FORMATS = [
    "mp4",   # MPEG-4 Video
    "avi",   # Audio Video Interleave
    "mkv",   # Matroska Video
    "mov",   # Apple QuickTime Movie
    "wmv",   # Windows Media Video
    "flv",   # Flash Video
    "webm",  # WebM Video
    "mpeg",  # MPEG Video
    "mpg",   # MPEG Video
    "m4v",   # MPEG-4 Video
    "3gp",   # 3GPP Multimedia File
    "3g2",   # 3GPP2 Multimedia File
    "vob",   # DVD Video Object
    "ogv",   # Ogg Video
    "rm",    # RealMedia
    "rmvb",  # RealMedia Variable Bitrate
    "asf",   # Advanced Systems Format
    "f4v",   # Flash MP4 Video
    "m2ts",  # Blu-ray Disc Audio-Video
    "mts"    # AVCHD Video
]

AUDIO_FORMATS = [
    "mp3",  # MPEG Layer 3 Audio
    "wav",  # Waveform Audio File Format
    "aac",  # Advanced Audio Coding
    "flac", # Free Lossless Audio Codec
    "alac", # Apple Lossless Audio Codec
    "ogg",  # Ogg Vorbis
    "wma",  # Windows Media Audio
    "aiff", # Audio Interchange File Format
    "m4a",  # MPEG-4 Audio
    "pcm",  # Pulse-Code Modulation
    "aif",  # Audio Interchange File Format
    "dsd",  # Direct Stream Digital
    "amr",  # Adaptive Multi-Rate Audio Codec
    "opus", # Opus Audio Codec
    "ra",   # Real Audio
    "au",   # Audio file format developed by Sun Microsystems
    "tta",  # True Audio
    "voc",  # Creative Labs Audio File
    "mid"   # MIDI (Musical Instrument Digital Interface)
]

IMG_FORMATS = [
    "jpg",  # JPEG image
    "jpeg", # JPEG image
    "png",  # Portable Network Graphics
    "gif",  # Graphics Interchange Format
    "bmp",  # Bitmap image
    "tiff", # Tagged Image File Format
    "tif",  # Tagged Image File Format
    "webp", # WebP image
    "svg",  # Scalable Vector Graphics
    "heic", # High Efficiency Image Coding
    "heif", # High Efficiency Image Format
    "raw",  # Raw image format
    "ico",  # Icon file format
    "psd",  # Adobe Photoshop Document
    "ai",   # Adobe Illustrator Artwork
    "eps",  # Encapsulated PostScript
    "pdf",  # Portable Document Format (can contain images)
    "indd", # Adobe InDesign Document
    "jfif"  # JPEG File Interchange Format
]

TXT_FORMATS = [
    "txt",  # Plain text file
    "md",   # Markdown file
    "html", # Hypertext Markup Language file
    "htm",  # Hypertext Markup Language file
    "css",  # Cascading Style Sheets file
    "js",   # JavaScript file
    "json", # JavaScript Object Notation file
    "xml",  # Extensible Markup Language file
    "csv",  # Comma-Separated Values file
    "tsv",  # Tab-Separated Values file
    "yaml", # YAML Ain't Markup Language file
    "yml",  # YAML Ain't Markup Language file
    "ini",  # Initialization file
    "log",  # Log file
    "rtf",  # Rich Text Format file
    "docx", # Microsoft Word document (text-based content)
    "odt",  # OpenDocument Text document
    "tex",  # LaTeX file
    "pdf"   # Portable Document Format (can contain text)
]

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
PIXEL_WIDTH, PIXEL_HEIGHT = 4, 1


# Modes for the creation of images (with PIL)

MODES = {
    1 : "1",    # Black and white
    8 : "L",    # Grayscale
    24 : "RGB", # Red-Green-Blue
    32 : "RGBA", # Red-Green-Blue-Transparency
}

# Maximun distance of two values in RGB format: 255**2 + 255**2 + 255**2
MAX_DIST = 195075