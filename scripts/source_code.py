from scripts.misc import *
from typing import List

class SourceCode:
    """
    A class to represent the source code of a source.

        Attributes
        ----------

        symbols1 : List["str"]
            List with symbols (domain)
        symbols2 : List["str"]
            List with symbols (range)
        map : dict
            Dictionary with the domain symbols (keys) and the range symbols (values)

        Methods
        -------

        __str__(self) -> str:
            Represents the source code in a string format.
        __repr__(self) -> str:
            Represents the source code in a string format for data structures.
        inverse(self) -> "SourceCode":
            Get inverse source code.
        average_length(self, source: "Source") -> float:
            Get the average length of the source code.
        source_code_to_string(self, length: int) -> str:
            Convert the source code object into a string object with then next format:
    """

    def __init__(self, symbols1: List["str"],  symbols2: List["str"]) -> None:
        self.symbols1, self.symbols2 = symbols1, symbols2
        self.map = dict(zip(self.symbols1, self.symbols2))

    def __str__(self) -> str:
        """
        Represents the source code in a string format.

            Parameters
                None
    
            Returns
                return The string format of the source code
        """

        return str(self.map)

    def __repr__(self) -> str:
        """
        Represents the source code in a string format for data structures.

            Parameters
                None
    
            Returns
                return The string format of the source code
        """

        return str(self.map)

    def inverse(self) -> "SourceCode":
        """
        Get inverse source code.

            Parameters
                None
    
            Returns
                return The inverse SourceCode
        """

        return SourceCode(self.symbols2, self.symbols1)

    def average_length(self, source: "Source") -> float:
        """
        Get the average length of the source code.

            Parameters
                source ("Source"): The Source (text file)

            Returns
                return A float representing the average length of the source code
        """

        return sum([source.pd[i]*len(self.symbols2[i]) for i in range(len(source.symbols))])

    def source_code_to_string(self, length: int) -> str:
        """
        Convert the source code object into a string object with the next format:
            value + length of the key (in bits) + key

            Parameters
                length (int): length to fit the binary string
    
            Returns
                return String source code format
        """

        sc_to_string = ""
        # Assert self.map[key] is a character
        for key in self.map:
            sc_to_string += character_to_binary(self.map[key], length) + int_to_bin_left_padding(len(key), length) + key
        return sc_to_string
