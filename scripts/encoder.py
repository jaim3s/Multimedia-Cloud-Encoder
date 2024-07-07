from scripts.entity import Entity
from scripts.encoders.huffman import Huffman
from scripts.source import Source
import scripts.constants


class Encoder(Entity):
    """
    A class to encode the content of the text file with a given coding method.

        Attributes
        ----------

        coding_method : str
            Name of the coding method to use
        source : "Source" 
            Source of the text file (Symbols, Probability Distribution)
        args : tuple
            Extra arguments of the coding method
        encoder : Object 
            Conding method to encode the file content
        source_code : "SourceCode"
            Source code from the encoder

        Methods
        -------
        
        check_coding_method(self) -> bool:
            Check if the coding method exist.
        select_coding_method(self) -> object:
            Select the coding method.
        add_redundancy(self, coded_content: str, bit_width: int) -> str:
            Add redundancy to the coded content.
        encode(self, content: str) -> str:
            Encode the content.
    """

    valid_kwargs = {
        "coding_method" : str,
        "source"        : Source,
        "args"          : list
    }

    def __init__(self, **kwargs: dict) -> None:
        # Validate the kwargs arguments
        self.validate_kwargs(kwargs, self.valid_kwargs) 
        self.encoder = self.select_coding_method()
        self.source_code = self.encoder.get_source_code()

    def check_coding_method(self) -> bool:
        """
        Check if the coding method exist.

            Parameters
                None

            Returns
                return The coding method object or raise an Exception
        """

        return self.coding_method in scripts.constants.CODING_METHODS

    def select_coding_method(self) -> object:
        """
        Select the coding method.

            Parameters
                None

            Returns
                return The coding method object or raise an Exception
        """

        if self.check_coding_method() == True:
            return scripts.constants.CODING_METHODS[self.coding_method](self.source, *self.args)
        else:
            raise Exception(f"Coding method ({self.coding_method}) doesn't exist.")

    def add_redundancy(self, coded_content: str, bit_width: int) -> str:
        """
        Add redundancy to the coded content.

            Parameters
                coded_content (str): The coded content of the image of the text file
                bit_width (int): Width of the bit

            Returns
                return The new coded content with redundancy
        """

        new_coded_content = ""
        for bit in coded_content:
            new_coded_content += bit*bit_width
        return new_coded_content

    def encode(self, content: str) -> str:
        """
        Encode the content.

            Parameters
                content (str): Text file content to encode

            Returns
                return The encoded content
        """

        encoded_content = "" 
        for ch in content:
            encoded_content += self.source_code.map[ch]
        return encoded_content
