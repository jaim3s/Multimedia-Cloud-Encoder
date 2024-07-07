from collections import Counter
from scripts.misc import *
from PIL import Image
import io, os, scripts.constants


class FileManager:
    """
    A class to manage the content of the text file.

        Attributes
        ----------

        file_path : str
            Path of the text file
        occurrences : dict
            Dictionary with the unique symbols and the ocurrences
        symbols : list
            List of unique symbols from the text file
        end_delimiter : str
            End delimiter of the text file content
        content : str
            Content of the text file
        length : int
            Total number of characters in the content of the text file

        Methods
        -------

        check_file_path(self, file_path: str) -> bool:
            Check if the file path exist.
        get_file_format(self) -> str:
            Get the file format from the file path.
        get_img_content(self) -> str:
            Get the image in string format.
        get_audio_content(self) -> str:
            Get the audio in string format.
        get_video_content(self) -> str:
            Get the video in string format.
        get_text_content(self) -> str:
            Get the content of the text file.
        get_occurrences(self) -> dict:
            Get the unique symbols and number occurences from the file path.
        get_total_length(self) -> int:
            Get the total length of the text file.
        get_probability_distribution(self) -> list:
            Get the probability distribution of the text file.
        get_unique_symbol(self) -> str:
            Get a unique printable character.
        convert(self, file_format: str) -> None:
            Convert the file to text file.
        initialization(self) -> None:
            Initializate the file manager.
    """

    def __init__(self, file_path: str) -> None:
        self.initialization(file_path) 

    def check_file_path(self, file_path: str) -> bool:
        """
        Check if the file path exist.

            Parameters
                file_path (str): The file path of the text file

            Returns
                return True if the file exist otherwise False
        """

        return not os.path.exists(file_path)

    def get_file_format(self) -> str:
        """
        Get the file format from the file path.

            Parameters
                None

            Returns
                return File format as a string
        """

        return self.file_path[self.file_path.rfind(".")+1:]

    def get_img_content(self) -> str:
        """
        Get the image in string format.

            Parameters
                None

            Returns
                return The image in the string format
        """

        byte_img_IO = io.BytesIO()
        byte_img = Image.open(self.file_path)
        byte_img.save(byte_img_IO, "PNG")
        byte_img_IO.seek(0)
        byte_img = byte_img_IO.read()
        return str(byte_img)

    def get_audio_content(self) -> str:
        """
        Get the audio in string format.

            Parameters
                None

            Returns
                return The audio in the string format
        """

        pass

    def get_video_content(self) -> str:
        """
        Get the video in string format.

            Parameters
                None

            Returns
                return The video in the string format
        """

        pass

    def get_text_content(self) -> str:
        """
        Get the content of the text file.

            Parameters
                None

            Returns
                return The content of the text file
        """

        content = ""
        with open(self.file_path, 'r', encoding="utf-8") as file:
            content = file.read()
        return content

    def get_occurrences(self) -> Counter:
        """
        Get the unique symbols and number occurences from the file path.

            Parameters
                None

            Returns
                return A Counter with the unique symbols (keys) and the number of occurrences of each symbol (values)
        """

        occurrences = Counter()
        with open(self.file_path, 'r', encoding='utf-8') as file:
            while chunk := file.read(8192):  # Read in chunks of 8KB
                occurrences.update(chunk)
        return occurrences

    def get_total_length(self) -> int:
        """
        Get the total length of the text file.

            Parameters
                None

            Returns
                return An integer with the total length of the text file
        """

        return sum(self.occurrences.values())

    def get_probability_distribution(self) -> list:
        """
        Get the probability distribution of the text file.

            Parameters
                None

            Returns
                return A list with the probabilities of each symbol in terms of the length of the text file
        """

        return [self.occurrences[key]/self.length for key in self.symbols]

    def get_unique_symbol(self) -> str:
        """
        Get a unique printable symbol.

            Parameters
                None

            Returns
                return A unique printable ASCII symbol, or None if all symbols are used.
        """

        for symbol in scripts.constants.ASCII_PRINTABLE_SYMBOLS:
            if symbol not in self.symbols:
                return symbol
        return None

    def convert(self) -> None:
        """
        Convert the file to text file.

            Parameters
                None

            Returns
                return None
        """

        if self.file_format in scripts.constants.TXT_FORMATS:
            return self.get_text_content()
        elif self.file_format in scripts.constants.IMG_FORMATS:
            return self.get_img_content()
        elif self.file_format in scripts.constants.AUDIO_FORMATS:
            return self.get_audio_content()
        elif self.file_format in scripts.constants.VIDEO_FORMATS:
            return self.get_video_content()
        else:
            raise Exception(f"The file format ({self.file_format}) isn't available.")  

    def initialization(self, file_path: str) -> None:
        """
        Initializate the file manager.

            Parameters
                file_path (str): File path

            Returns
                return None
        """

        if self.check_file_path(file_path):
            raise Exception(f"The file path ({file_path}) doesn't exist.")  
        self.file_path = file_path
        self.file_format = self.get_file_format()
        self.content = self.convert()
        self.occurrences = self.get_occurrences()
        self.symbols = list(self.occurrences.keys())
        self.end_delimiter = self.get_unique_symbol()
        if not self.end_delimiter:
            raise Exception(f"The delimiter ({self.end_delimiter}) is in the content of the file, this can produce ambiguity.")
        # Add the new symbol (end delimiter)
        self.occurrences[self.end_delimiter] = 1
        self.symbols.append(self.end_delimiter)
        self.content += self.end_delimiter
        self.length = self.get_total_length()


       