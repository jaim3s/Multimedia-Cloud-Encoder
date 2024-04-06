from scripts.constants import *
from scripts.encoders.huffman import Huffman

class Encoder:
    """
    A class to encode the content of the text file.

        Attributes
        ----------

        coding_method : str
            Name of the coding method to use
        source : "Source" 
            Source of the text file (Symbols, Probability distribution)
        args : tuple
            Extra arguments of the coding method
        encoder : Object 
            Get the encoder to encode the file content
        source_code : "SourceCode"
            Get the source code from the encoder

        Methods
        -------

        select_coding_method(self) -> object:
            Select the coding method.
        encode(self, content: str) -> str:
            Encode the content.
    """

    def __init__(self, coding_method: str, source: "Source", *args: tuple) -> None:
        self.coding_method = coding_method.lower()
        self.source = source
        self.args = list(args)
        self.encoder = self.select_coding_method()
        # All the coding methods need the function of get source code
        self.source_code = self.encoder.get_source_code()

    def select_coding_method(self) -> object:
        """
        Select the coding method.

            Parameters
                None

            Returns
                return The coding method object or raise an Exception
        """

        if self.coding_method in CODING_METHODS:
            return CODING_METHODS[self.coding_method](self.source, *self.args)
        raise Exception("Coding method doesn't exist.")

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
