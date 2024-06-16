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

    def compare(self) -> None:
        """
        Compare the programs metrics.

            Parameters
                None
    
            Returns
                return None
        """

        data = {}
        for key in self.programs[0].metrics:
            data[key] = [program.metrics[key] for program in self.programs]
        df = pd.DataFrame(data)
        print(df)
                
