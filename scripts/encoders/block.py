from scripts.source_code import SourceCode
from scripts.encoders.coding_method import CodingMethod
from scripts.misc import *
from typing import List
from math import ceil, log

class Block(CodingMethod):
    """
    A class of the Block code method.

        Attributes
        ----------

        source : "Source" 
            Source of the text file (Symbols, Probability Distribution)
        output_symbols : List[str]
            The output symbols of the coding method
        d : int
            The arity of the Block code 
        n : int
            Number of symbols

        Methods
        -------

        __str__(self) -> str:
            Represents the Block codification in a string format.
        __repr__(self) -> str:
            Represents the Block codification in a string format for data structures.
        run(self) -> List[str]:
            Execute the entire Block codification algorihtm.
        get_source_code(self) -> "SourceCode":
            Get the source code from the Block code.
    """

    def __init__(self, source: "Source", output_symbols: List[str]) -> None: 
        super().__init__(source)
        self.output_symbols = output_symbols
        self.d = len(self.output_symbols)
        self.n = len(self.source.symbols)

    def __str__(self) -> str:
        """
        Represents the block code in a string format.

            Parameters
                None
    
            Returns
                return The string format of the block codification
        """

        return self.source.__str__()

    def __repr__(self) -> str:
        """
        Represents the block code in a string format for data structures.

            Parameters
                None
    
            Returns
                return The string format of the block codification
        """

        return self.source.__str__()

    def run(self) -> List[str]:
        """
        Execute the entire Huffman codification algorihtm.

            Parameters
                None
    
            Returns
                return The root of the tree
        """

        block_length = ceil(log(self.n, self.d))
        num_code_words = 2**block_length
        return [int_to_bin_left_padding(code_word, block_length) for code_word in range(num_code_words)]


    def get_source_code(self) -> "SourceCode":
        """
        Get the source code from the Huffman code.

            Parameters
                None
    
            Returns
                return Source code of the Huffman code
        """

        return SourceCode(self.source.symbols, self.run())
