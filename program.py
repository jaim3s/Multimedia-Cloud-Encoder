from file_manager import FileManager
from source import Source
from huffman import Huffman
from encoder import Encoder
from decoder import Decoder
from image_generator import ImageGenerator
from math import ceil
from constants import *

class Program:
    def __init__(self, file_path: str, coding_method: str) -> None:
        self.file_manager = FileManager(file_path)
        self.file_path = file_path
        self.coding_method = coding_method

    def run(self) -> None:

        # Get the probability distribution and create the source
        pd = self.file_manager.get_pd()
        source = Source(list(self.file_manager.symbols), pd)
        content = self.file_manager.get_content()

        T = ["0", "1"]
        encoder = Encoder(self.coding_method, source, T)
        source_code = encoder.source_code
        average_length = source_code.average_length(source)
        entropy = source.entropy(len(T))
        coded_content = encoder.encode(content)

        # Image generator
        image = ImageGenerator(coded_content, BIT_DEPTH)
        image.save("imgs/frame1.png")
        
        # Decoder
        inverse_source_code = source_code.inverse()
        decoder = Decoder("imgs/frame1.png", ceil(len(coded_content)/image.bit_depth), inverse_source_code)
        decoder_content = decoder.decode(coded_content)

        print(decoder_content == content)

        # Print basic information about the file
        print("File path:", self.file_path)
        print("Coding method:", self.coding_method)
        print("Number of unique symbols:", len(self.file_manager.symbols))
        print("Number of characters:", self.file_manager.length)

        # Print information about the source code and the source
        print("Average word length:", average_length)
        print("Entropy:", entropy)
        print("Efficiency", entropy/average_length)

        # Print information 
        print("Number of pixels:", image.total_pixels)
        print("Image dimensions:", image.width, image.height)


