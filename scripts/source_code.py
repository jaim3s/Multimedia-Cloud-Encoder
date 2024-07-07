from scripts.entity import Entity
from scripts.misc import *
from typing import List


class SourceCode(Entity):
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

    valid_kwargs = {
        "symbols1" : list,
        "symbols2" : list,
    }

    def __init__(self, **kwargs: dict) -> None:
        # Validate the kwargs arguments
        self.validate_kwargs(kwargs, self.valid_kwargs) 
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

        return SourceCode(
            symbols1=self.symbols2, 
            symbols2=self.symbols1
        )

    def average_length(self, source: "Source") -> float:
        """
        Get the average length of the source code.

            Parameters
                source ("Source"): The Source (text file)

            Returns
                return A float representing the average length of the source code
        """

        return sum([source.probability_distribution[i]*len(self.symbols2[i]) for i in range(len(source.symbols))])

    def inverse_source_code_to_string(self, length: int) -> str:
        """
        Convert the source code object into a string object with the next format:
            value + length of the key (in bits) + key

            Parameters
                length (int): Length to fit the binary string
    
            Returns
                return String source code format
        """

        sc_to_string = ""
        for key in self.map:
            sc_to_string += character_to_binary(self.map[key], length) + int_to_bin_left_padding(len(key), length) + key
        return sc_to_string
