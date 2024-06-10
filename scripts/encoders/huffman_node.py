class HuffmanNode:
    """
    A class of the Huffman nodes.

        Attributes
        ----------

        symbol : str 
            Symbol of the Huffman node
        probability : float
            Probability of the Huffman node
        active : bool
            Current state of the Huffman node
        childs : List["HuffmanNode"]
            Childs of the Huffman node
        mark : str
            Current name of the Huffman node

        Methods
        -------

        __str__(self) -> str:
            Represents the Huffman node in a string format.
        __repr__(self) -> str:
            Represents the Huffman node in a string format for data structures.
    """

    def __init__(self, symbol: str, probability: float) -> None:
        self.symbol = symbol
        self.probability = probability
        self.active = True
        self.childs = []
        self.mark = ""

    def __str__(self) -> str:
        """
        Represents the Huffman node in a string format.

            Parameters
                None
    
            Returns
                return The string format of the huffman codification
        """

        return str(self.symbol)

    def __repr__(self) -> str:
        """
        Represents the Huffman node in a string format for data structures.

            Parameters
                None
    
            Returns
                return The string format of the huffman codification
        """

        return str(self.symbol)