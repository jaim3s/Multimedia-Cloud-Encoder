class CodingMethod:
    """
    A class to represent the coding methods.

        Attributes
        ----------

        source : "Source" 
            Source of the text file (Symbols, Probability Distribution)

        Methods
        -------

        __str__(self) -> str:
            Represents the coding method in a string format.
        __repr__(self) -> str:
            Represents the coding method in a string format for data structures.
        get_source_code(self) -> None:
            Get the source code from the coding method.
    """

    def __init__(self, source: "Source") -> None:
        self.source = source

    def __str__(self) -> str:
        """
        Represents the coding method in a string format.

            Parameters
                None
    
            Returns
                return The string format of the huffman codification
        """

        return self.source.__str__()

    def __repr__(self) -> str:
        """
        Represents the coding method in a string format for data structures.

            Parameters
                None
    
            Returns
                return The string format of the huffman codification
        """

        return self.source.__repr__()

    def get_source_code(self) -> None:
        """
        Get the source code from the coding method.

            Parameters
                None
    
            Returns
                return None
        """

        return None
        