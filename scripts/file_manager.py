from scripts.misc import *
from PIL import Image
import scripts.constants
import io, os

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
            Check if the file exist.
        get_content(self) -> str:
            Get the content of the text file.
        get_occurrences(self) -> dict:
            Get the unique symbols and number occurences from the file path.
        get_total_length(self) -> int:
            Get the total length of the text file.
        get_pd(self) -> list:
            Get the probability distribution of the text file.
        get_unique_symbol(self) -> str:
            Get a unique printable character.
    """

    def __init__(self, file_path: str) -> None:
        if self.check_file_path(file_path):
            raise Exception(f"The file path ({file_path}) doesn't exist.")
        self.file_path = file_path
        self.format = self.file_path[self.file_path.rfind(".")+1:]
        # Get the content from the text file or image file
        if self.format in scripts.constants.IMG_FORMATS:
            self.content = self.convert_img_to_string()
        elif self.format in scripts.constants.TXT_FORMATS:
            self.content = self.get_content()
        self.occurrences = self.get_occurrences()
        self.symbols = list(self.occurrences.keys())
        self.end_delimiter = self.get_unique_symbol()
        if not self.end_delimiter:
            raise Exception(f"The delimiter ({self.end_delimiter}) is in the content of the file, this can produce ambiguity.")
        # Add the new symbol
        self.occurrences[self.end_delimiter] = 1
        self.symbols.append(self.end_delimiter)
        self.content += self.end_delimiter
        self.length = self.get_total_length()

    def check_file_path(self, file_path: str) -> bool:
        """
        Check if the file exist.

            Parameters
                file_path (str): The file path of the text file

            Returns
                return True if the file exist otherwise False
        """

        return not os.path.exists(file_path)

    def convert_img_to_string(self) -> str:
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

    def get_content(self) -> str:
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

    def get_occurrences(self) -> dict:
        """
        Get the unique symbols and number occurences from the file path.

            Parameters
                None

            Returns
                return A dictionary with the unique symbols (keys) and the number of occurrences of each symbol (values)
        """

        occurrences = {}
        with open(self.file_path, 'r', encoding="utf-8") as file:
            char = file.read(1)
            while char:
                if char in occurrences:
                    occurrences[char] += 1
                else:
                    occurrences[char] = 1
                char = file.read(1)
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

    def get_pd(self) -> list:
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