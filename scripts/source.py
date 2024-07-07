from scripts.entity import Entity
from typing import List
from math import log


class Source(Entity):
    """
    A class to represent the source of a text file.

        Attributes
        ----------

        symbols : List["str"]
            List with symbols
        probability_distribution : List[float]
            List wit the probability distribution
        source : dict
            Dictionary with the symbols (keys) and the probability distribution (values)

        Methods
        -------

        __str__(self) -> str:
            Represents the source in a string format.
        __repr__(self) -> str:
            Represents the source in a string format for data structures.
        join(self) -> List:
            Join the symbols with it's probability.
        entropy(self, d: int) -> float:
            Get the entropy of the source.
    """

    valid_kwargs = {
        "symbols"                  : list,
        "probability_distribution" : list,
    }

    def __init__(self, **kwargs: dict) -> None:
        # Validate the kwargs arguments
        self.validate_kwargs(kwargs, self.valid_kwargs) 
        self.source = self.join()

    def __str__(self) -> str:
        """
        Represents the source in a string format.

            Parameters
                None
    
            Returns
                return The string format of the source
        """

        return str(self.source)

    def __repr__(self) -> str:
        """
        Represents the source in a string format for data structures.

            Parameters
                None
    
            Returns
                return The string format of the source
        """

        return str(self.source)

    def join(self) -> List:
        """
        Join the symbols with it's probability.

            Parameters
                None
    
            Returns
                return List with the each symbol and it's probability
        """

        return list(zip(self.symbols, self.probability_distribution))

    def entropy(self, d: int) -> float:
        """
        Get the entropy of the source.

            Parameters
                d (int): The arity of codification

            Returns
                return A float representing the entropy
        """

        return -sum([self.probability_distribution[i]*log(self.probability_distribution[i], d) for i in range(len(self.symbols))])


