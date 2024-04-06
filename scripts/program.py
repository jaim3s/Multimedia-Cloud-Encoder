from scripts.file_manager import FileManager
from scripts.source import Source
from scripts.encoders.huffman import Huffman
from scripts.encoder import Encoder
from scripts.decoder import Decoder
from scripts.video_generator import VideoGenerator
from scripts.constants import *
from scripts.misc import *
from math import ceil
import os

class Program:
    """
    A class to execute the program.

        Attributes
        ----------

        file_manager : FileManager
            Text file manager
        file_path : str
            Path of the text file
        coding_method : str
            Name of the coding method to use
        args : tuple
            Extra arguments of the coding method

        Methods
        -------

        log(self, content: str) -> None:
            Create a file to write the given content.
        delete_files_in_folder(self, folder_path: str) -> None:
            Delete all the files of a given folder path.
        run(self) -> None:
            Run the program.
    """

    def __init__(self, file_path: str, coding_method: str, *args: tuple) -> None:
        self.file_manager = FileManager(file_path)
        self.file_path = file_path
        self.coding_method = coding_method
        self.args = list(args)

    def log(self, content: str) -> None:
        """
        Create a file to write the given content.

            Parameters
                content (str): Content to write in the log file
    
            Returns
                return None
        """

        with open(logs_text_file_path, "w") as file:
            file.write(content)

    def delete_files_in_folder(self, folder_path: str) -> None:
        """
        Delete all the files of a given folder path.

            Parameters
                folder_path (str): Path of the folder
    
            Returns
                return None
        """

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
        """
        Run the program.

            Parameters
                None
    
            Returns
                return None
        """

        # Delete all the files of the folder imgs_folder_path
        self.delete_files_in_folder(imgs_folder_path)

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
