import os

class FileManager:
    def __init__(self, file_path: str) -> None:
        if self.check_file_path(file_path):
            raise Exception("File doesn't exist.")
        self.file_path = file_path
        self.content = self.get_content()
        self.info = self.get_information()
        self.symbols = self.info.keys()
        self.length = self.get_total_length()

    def check_file_path(self, file_path: str) -> bool:
        """
        Check if the file exist.

            Parameters
                file_path (str): The file path of the text file

            Returns
                return True if the file exist otherwise False
        """

        return not os.path.exists(file_path)

    def get_content(self) -> str:
        """
        Get the content of the text file.

            Parameters
                None

            Returns
                return The content of the text file
        """

        content = ""
        with open(self.file_path, 'r') as file:
            content = file.read()
        return content

    def get_information(self) -> dict:
        """
        Get the unique symbols and number occurences from the file path.

            Parameters
                None

            Returns
                return A dictionary with the unique symbols (keys) and the number of occurrences of each symbol (values)
        """

        info = {}
        with open(self.file_path, 'r') as file:
            char = file.read(1)
            while char:
                if char in info:
                    info[char] += 1
                else:
                    info[char] = 1
                char = file.read(1)
        return info

    def get_total_length(self) -> int:
        """
        Get the total length of the text file.

            Parameters
                None

            Returns
                return An integer with the total length of the text file
        """

        return sum(self.info.values())

    def get_pd(self) -> list:
        """
        Get the probability distribution of the text file.

            Parameters
                None

            Returns
                return A list with the probabilities of each symbol in terms of the length of the text file
        """

        return [self.info[key]/self.length for key in self.info]
