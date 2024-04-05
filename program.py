from file_manager import FileManager
from source import Source
from huffman import Huffman
from encoder import Encoder
from decoder import Decoder
from video_generator import VideoGenerator
from math import ceil
from constants import *
from misc import *
import os

class Program:
    def __init__(self, file_path: str, coding_method: str) -> None:
        self.file_manager = FileManager(file_path)
        self.file_path = file_path
        self.coding_method = coding_method

    def log(self, content: str) -> None:
        with open('logs/log.txt', 'w') as file:
            file.write(content)

    def difference(self, file_path1: str, file_path2: str) -> None:
        indx = []
        with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
            content1, content2 = file1.read(), file2.read()

    def delete_files_in_folder(self, folder_path: str) -> None:
        # Iterate over all the files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)  # Delete the file
                    print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

    def run(self) -> None:

        # Delete all the files of the folder /imgs
        self.delete_files_in_folder("imgs/")

        # Get the probability distribution and create the source
        pd = self.file_manager.get_pd()
        content = self.file_manager.content
        source = Source(self.file_manager.symbols, pd)

        T = ["0", "1"]
        encoder = Encoder(self.coding_method, source, T)
        source_code = encoder.source_code
        inverse_source_code = source_code.inverse()

        # Get the inverse source code in string format
        inverse_source_code_str = inverse_source_code.source_code_to_string(BLOCK_CODE_LENGTH)
        
        # Average word length and entropy of the source and source code
        average_length = source_code.average_length(source)
        entropy = source.entropy(len(T))

        # Add the inverse source code to the coded content of the text file and the delimiters
        coded_content = inverse_source_code_str + character_to_binary(SOURCE_CODE_DELIMITER, BLOCK_CODE_LENGTH) + encoder.encode(content) 

        # Video generator
        video = VideoGenerator(coded_content, BIT_DEPTH)
        video.save("imgs/")

        # Decoder
        decoder = Decoder("imgs/")

        coded_content_decoder = decoder.get_coded_content()

        decoder_content = decoder.decode(coded_content_decoder)

        print(content[:-1] == decoder_content)

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
        print("Number of pixels:", video.total_pixels)
        print("Image dimensions:", video.width, video.height)

