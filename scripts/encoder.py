import scripts.constants
from scripts.encoders.huffman import Huffman

class Encoder:
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

        select_coding_method(self) -> object:
            Select the coding method.
        add_redundancy(self, coded_content: str, pixel_width: int) -> str:
            Add redundancy to the coded content.
        encode(self, content: str) -> str:
            Encode the content.
    """

    def __init__(self, coding_method: str, source: "Source", args: list) -> None:
        self.coding_method = coding_method.lower()
        self.source = source
        self.args = args
        self.encoder = self.select_coding_method()
        self.source_code = self.encoder.get_source_code()

    def select_coding_method(self) -> object:
        """
        Select the coding method.

            Parameters
                None

            Returns
                return The coding method object or raise an Exception
        """

        if self.coding_method in scripts.constants.CODING_METHODS:
            if scripts.constants.CODING_METHODS.get(self.coding_method, None):
                return scripts.constants.CODING_METHODS[self.coding_method](self.source, *self.args)
            else:
                raise Exception(f"Coding method ({self.coding_method}) doesn't exist.")

    def add_redundancy(self, coded_content: str, pixel_width: int) -> str:
        """
        Add redundancy to the coded content.

            Parameters
                coded_content (str): The coded content from the image of the text file
                pixel_width (int): Width of the pixels

            Returns
                return The new coded content with redundancy
        """

        new_coded_content = ""
        for ch in coded_content:
            new_coded_content += ch*pixel_width
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
