import pandas as pd

class Comparator:

    def compare(self, program0: "Program", program1: "Program") -> None:
        """
        Compare two programs metrics.

            Parameters
                program0 ("Program"): First program 
                program1 ("Program"): Second program
    
            Returns
                return None
        """

        data = {}

        for key in program0.metrics:
            data[key] = [program0.metrics[key], program1.metrics[key]]
        df = pd.DataFrame(data)

        # Display dataframe information
        print(df)

