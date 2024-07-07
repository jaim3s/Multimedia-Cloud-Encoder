from scripts.file_manager import FileManager
from scripts.source import Source
from scripts.encoders.huffman import Huffman
from scripts.encoder import Encoder
from scripts.decoder import Decoder
from scripts.video_generator import VideoGenerator
from scripts.image_comparator import ImageComparator
from scripts.entity import Entity
from scripts.misc import *
from math import ceil
from typing import List, Tuple
import scripts.constants, os, numpy as np


class Program(Entity):
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

        create_paths(self) -> None:
            Create the paths of the Program object.
        create_folders(self) -> None:
            Create the folders of the Program object.
        log(self, content: str) -> None:
            Create a file to write the given content.
        delete_files_in_folder(self, folder_path: str) -> None:
            Delete all the files of a given folder path.
        get_metrics(self) -> None:
            Get the metrics.
        generate_results(self) -> str:
            Generate the final results.
        initialization(self) -> None:
            Initializate the program.
        run(self) -> None:
            Run the program.
    """

    valid_kwargs = {
        "file_path"     : str,
        "coding_method" : str,
        "platform"      : str,
        "bit_width"     : int,
        "bit_height"    : int,
        "args"          : list,
    }

    def __init__(self, **kwargs: dict) -> None:
        # Validate the kwargs arguments
        self.validate_kwargs(kwargs, self.valid_kwargs) 
        self.initialization()

    def create_paths(self) -> None:
        """
        Create the paths of the Program object.

            Parameters
                None
    
            Returns
                return None
        """

        # Define the parent path
        self.parent_path = scripts.constants.content_folder_path + "\\" + self.coding_method

        # Images path (general, original frames and video frames)
        self.imgs_path = self.parent_path + "\\imgs"
        self.original_frames_path = self.imgs_path + "\\original_frames"
        self.video_frames_path = self.imgs_path + "\\video_frames"

        # Video path
        self.video_path = self.parent_path + "\\video"

        # Comparison path
        self.comparison_path = self.imgs_path + "\\comparison"

        # Log path
        self.log_path = self.parent_path + "\\logs"

    def create_folders(self) -> None:
        """
        Create the folders of the Program object.

            Parameters
                None
    
            Returns
                return None
        """

        os.makedirs(self.parent_path, exist_ok=True)
        os.makedirs(self.imgs_path, exist_ok=True)
        os.makedirs(self.video_path, exist_ok=True)
        os.makedirs(self.original_frames_path, exist_ok=True)
        os.makedirs(self.video_frames_path, exist_ok=True)
        os.makedirs(self.comparison_path, exist_ok=True)
        os.makedirs(self.log_path, exist_ok=True)

    def log(self, filename: str, content: str) -> None:
        """
        Create a file to write the given content.

            Parameters
                filename (str): Name of the logs file
                content (str): Content to write in the log file
    
            Returns
                return None
        """

        with open(self.log_path + f"\\{filename}", "w") as file:
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

    def get_metrics(self) -> str:
        """
        Get the metrics.

            Parameters
                None
    
            Returns
                return The metrics of the program in string format
        """

        res = ""
        for key in self.metrics:
            res += key + ":" + str(self.metrics[key]) + "\n"
        return res

    def generate_results(self, decoder_content: str, comparisons: List[np.ndarray]) -> str:
        """
        Generate the final results.

            Parameters
                decoder_content (str): Final result of the code
    
            Returns
                return The results of the Program execution.
        """

        result = f"Basic information - {self.coding_method}\n"
        result += "Result: True\n" if self.file_manager.content[:-1] == decoder_content else "Result: False\n"
        result += "File path: " + self.file_manager.file_path + "\n"
        result += "Coding method: " + self.coding_method + "\n"
        result += "Unique characters: " + str(len(self.file_manager.symbols)) + "\n"
        result += "Number of characters: " + str(self.file_manager.length) + "\n" 
        result += "Comparison: " + " ".join([str(comparison) for comparison in comparisons]) + "\n"
        result += "Metrics\n"
        return result

    def initialization(self) -> None:
        """
        Initializate the program.

            Parameters
                None
    
            Returns
                return None
        """

        # Create paths and folders
        self.create_paths()
        self.create_folders()

        self.file_manager = FileManager(self.file_path)
        self.metrics = {}

        # Assert lower case letters
        self.coding_method = self.coding_method.lower();

    def run(self) -> None:
        """
        Run the program.

            Parameters
                None
    
            Returns
                return None
        """

        # Get the probability distribution and create the source
        source = Source(
            symbols=self.file_manager.symbols, 
            probability_distribution=self.file_manager.get_probability_distribution()
        )
        
        # Get the content of the file
        content = self.file_manager.content

        # Create the encoder & get the source code 
        encoder = Encoder(
            coding_method=self.coding_method,
            source=source, 
            args=self.args
        )

        source_code = encoder.source_code
        inverse_source_code = source_code.inverse()

        # Get the inverse source code in string format
        inverse_source_code_str = inverse_source_code.inverse_source_code_to_string(scripts.constants.BLOCK_CODE_LENGTH)
        
        """
        
        # Average word length and entropy of the source and source code
        average_length = source_code.average_length(source)

        # The base of the entropy is 2
        entropy = source.entropy(scripts.constants.ENTROPY_ARITY)

        # Add the inverse source code to the coded content of the text file and the delimiters
        coded_content = inverse_source_code_str + character_to_binary(scripts.constants.SOURCE_CODE_DELIMITER, scripts.constants.BLOCK_CODE_LENGTH) + encoder.encode(content) 
        coded_content = encoder.add_redundancy(coded_content, self.bit_width)

        # Video generator in the platform of youtube
        video = VideoGenerator(
            coded_content = coded_content,
            bit_depth = scripts.constants.BIT_DEPTH,
            platform = self.platform.lower(),
            bit_width = self.bit_width,
            bit_height = self.bit_height,
            original_frames_path = self.original_frames_path,
            video_frames_path = self.video_frames_path,
            video_path = self.video_path,
        )

        # Decoder
        decoder = Decoder(self.original_frames_path)

        coded_content_decoder = decoder.get_coded_content()

        decoder_content = decoder.decode(coded_content_decoder)

        # Image comparison
        image_comparator = ImageComparator(
            self.original_frames_path,
            self.video_frames_path,
            self.comparison_path
        )
        image_comparator.compare()
        comparisons = image_comparator.average(image_comparator.comparisons)

        # Save basic metrics
        self.metrics["entropy"] = entropy
        self.metrics["average-length"] = average_length
        self.metrics["efficiency"] = entropy/average_length
        self.metrics["pixels"] = video.total_pixels
        self.metrics["dimensions"] = (video.width, video.height)
        
        result = self.generate_results(decoder_content, comparisons) + "\n" + self.get_metrics()
        self.log(f"log_{self.coding_method}.txt", result)
        """