from typing import List
import pandas as pd

class Comparator:
    """
    A class to compare two programs.

        Attributes
        ----------

        program0 : "Program"
            Program 0 
        program1 : "Program"
            Program 1 

        Methods
        -------

        compare(self) -> None:
            Compare the programs metrics.
    """

    def __init__(self, programs: List["Program"]) -> None:
        self.programs = programs

    def compare(self) -> pd.DataFrame:
        """
        Compare the programs metrics.

            Parameters
                None
    
            Returns
                return Dataframe with the metrics of each Program
        """

        data = {}
        for key in self.programs[0].metrics:
            data[key] = [program.metrics[key] for program in self.programs]
        return pd.DataFrame(data)
                
