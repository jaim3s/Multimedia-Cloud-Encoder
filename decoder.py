class Decoder:
    def __init__(self, img_path: str, n: int, inverse_source_code: "SourceCode") -> None:
        self.img_path = img_path
        self.n = n
        self.inverse_source_code = inverse_source_code

    def int_to_bin(self, num: int, n: int) -> str:
        """
        Convert integer to binary with n number of bits.

            Parameters
                num (int): Integer to convert
                n (int): Number of bits

            Returns
                return A string representing the binary number of the integer
        """

        return str(bin(num)[2:].zfill(n))

    def get_coded_content(self) -> str:
        """
        Get the coded content from the img_path.

            Parameters
                None

            Returns
                return The coded content
        """

        coded_content = ""
        pixel_array = list(Image.open(self.img_path).getdata())[:self.n]
        for pixel in pixel_array:
            for val in pixel:
                coded_content += self.int_to_bin(val, 8)
        return coded_content

    def decode(self, coded_content: str) -> str:
        """
        Decode the coded content.

            Parameters
                coded_content (str): The coded content of the text file

            Returns
                return The original coded content
        """

        content, sub = "", ""
        for ch in coded_content:
            sub += ch
            if sub in self.inverse_source_code.map:
                content += self.inverse_source_code.map[sub]
                sub = ""
        return content
