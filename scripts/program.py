from scripts.file_manager import FileManager
from scripts.source import Source
from scripts.encoders.huffman import Huffman
from scripts.encoder import Encoder
from scripts.decoder import Decoder
from scripts.video_generator import VideoGenerator
from scripts.misc import *
from math import ceil
from typing import Tuple
import scripts.constants, os
import numpy as np

class Program:
    """
    A class to execute the program.

        Attributes
        ----------
        
        valid_kwargs : dict
            Dictionary with the valid key word arguments
        file_path : str
            Path of the text file
        file_manager : FileManager
            Text file manager
        coding_method : str
            Name of the coding method to use
        args : tuple
            Extra arguments of the coding method
        metrics : dict
            Dictionary with the program metrics

        Methods
        -------

        validate_kwargs(self, kwargs: dict, valid_kwargs: dict) -> None:
            Validate the key word arguments.
        log(self, content: str) -> None:
            Create a file to write the given content.
        delete_files_in_folder(self, folder_path: str) -> None:
            Delete all the files of a given folder path.
        show_metrics(self) -> None:
            Show the metrics.
        run(self) -> None:
            Run the program.
    """

    valid_kwargs = {
        "file_path"       : str,
        "coding_method"   : str,
        "args"            : list,
    }

    def __init__(self, **kwargs) -> None:
        # Validate the kwargs arguments
        self.validate_kwargs(kwargs, self.valid_kwargs) 
        self.file_manager = FileManager(self.file_path)
        self.metrics = {}

    def validate_kwargs(self, kwargs: dict, valid_kwargs: dict) -> None:
        """
        Validate the key word arguments.

            Parameters
                kwargs (dict): Dictinoary with the key word arguments
                valid_kwargs (dict) : Dictionary with the allowed key word arguments
    
            Returns
                return None
        """

        for key in kwargs:
            # Validate key & value
            if valid_kwargs.get(key, None):
                if isinstance(kwargs[key], valid_kwargs[key]):
                    setattr(self, key, kwargs[key])
                else:
                    raise Exception(f"The attributes values ({kwargs[key]}) are invalid.")
            else:
                raise Exception(f"The key ({key}) ins't a valid keyword argument.")

    def log(self, content: str) -> None:
        """
        Create a file to write the given content.

            Parameters
                content (str): Content to write in the log file
    
            Returns
                return None
        """

        with open(scripts.constants.logs_text_file_path, "w") as file:
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

    def create_folder(self) -> None:

        # Define the paths
        self.parent_path = scripts.constants.content_folder_path + "\\" + self.coding_method

        # Images path
        self.imgs_path = self.parent_path + "\\imgs"
        self.original_frames_path = self.imgs_path + "\\original_frames"
        self.video_frames_path = self.imgs_path + "\\video_frames"

        # Video path
        self.video_path = self.parent_path + "\\video"

        # Create folders
        os.makedirs(self.parent_path, exist_ok=True)
        os.makedirs(self.imgs_path, exist_ok=True)
        os.makedirs(self.video_path, exist_ok=True)
        os.makedirs(self.original_frames_path, exist_ok=True)
        os.makedirs(self.video_frames_path, exist_ok=True)

    def show_metrics(self) -> None:
        """
        Show the metrics.

            Parameters
                None
    
            Returns
                return None
        """

        for key in self.metrics:
            print(key, ":", self.metrics[key])

    def run(self) -> None:
        """
        Run the program.

            Parameters
                None
    
            Returns
                return None
        """

        # Create directory
        self.create_folder()

        # Get the probability distribution and create the source
        pd = self.file_manager.get_pd()
        source = Source(self.file_manager.symbols, pd)
        
        # Get the content
        content = self.file_manager.content

        # Create the encoder & get the source code 
        encoder = Encoder(self.coding_method, source, self.args)
        
        source_code = encoder.source_code
        inverse_source_code = source_code.inverse()

        # Get the inverse source code in string format
        inverse_source_code_str = inverse_source_code.inverse_source_code_to_string(scripts.constants.BLOCK_CODE_LENGTH)
        
        # Average word length and entropy of the source and source code
        average_length = source_code.average_length(source)

        # The base of the entropy is 2
        entropy = source.entropy(scripts.constants.ENTROPY_ARITY)

        # Add the inverse source code to the coded content of the text file and the delimiters
        coded_content = inverse_source_code_str + character_to_binary(scripts.constants.SOURCE_CODE_DELIMITER, scripts.constants.BLOCK_CODE_LENGTH) + encoder.encode(content) 
        coded_content = encoder.add_redundancy(coded_content, scripts.constants.PIXEL_WIDTH)

        # Video generator in the platform of youtube
        video = VideoGenerator(
            coded_content, 
            scripts.constants.BIT_DEPTH,
            "youtube".lower(),
            self.original_frames_path,
            self.video_frames_path,
            self.video_path
        )

        # Decoder
        decoder = Decoder(self.original_frames_path)

        coded_content_decoder = decoder.get_coded_content()

        decoder_content = decoder.decode(coded_content_decoder)

        self.log(decoder_content)

        print("Basic information")
        print("Content = Decoded content?:", content[:-1] == decoder_content)
        print("File path:", self.file_manager.file_path)
        print("Coding method:", self.coding_method)
        print("Unique characters:", len(self.file_manager.symbols))
        print("Number of characters:", self.file_manager.length)

        # Save basic metrics
        self.metrics["entropy"] = entropy
        self.metrics["average-length"] = average_length
        self.metrics["efficiency"] = entropy/average_length
        self.metrics["pixels"] = video.total_pixels
        self.metrics["dimensions"] = (video.width, video.height)

        print("Metrics")

        self.show_metrics()
