from PIL import Image
from constants import *
from misc import *
import os

class Decoder:
    def __init__(self, folder_path: str) -> None:
        self.folder_path = folder_path

    def get_coded_content_from_img(self, file_path: str) -> str:
        """
        Get the coded content from the image.

            Parameters
                file_path (str): File path of the image

            Returns
                return The coded content from the image
        """

        coded_content = ""
        pixel_array = list(Image.open(file_path).getdata())
        for pixel in pixel_array:
            for val in pixel:
                coded_content += int_to_bin_left_padding(val, BITS_PER_CHANNEL)
        return coded_content

    def get_coded_content(self) -> str:
        coded_content = ""
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                coded_content += self.get_coded_content_from_img(file_path)
        return coded_content

    def decode(self, coded_content: str) -> str:
        """
        Decode the coded content.

            Parameters
                coded_content (str): The coded content from the image of the text file

            Returns
                return The original content
        """

        inverse_source_code = {}
        i = 0
        value = coded_content[i:i+BLOCK_CODE_LENGTH]
        # Get the inverse source code
        while value != character_to_binary(SOURCE_CODE_DELIMITER, BLOCK_CODE_LENGTH):
            length = int(coded_content[i+BLOCK_CODE_LENGTH:i+BLOCK_CODE_LENGTH*2], 2)
            key = coded_content[i+BLOCK_CODE_LENGTH*2:i+BLOCK_CODE_LENGTH*2+length]
            inverse_source_code[key] = binary_to_character(value)
            i = i+BLOCK_CODE_LENGTH*2+length
            value = coded_content[i:i+BLOCK_CODE_LENGTH]
        # From here start the coded content of the text file
        i = i+BLOCK_CODE_LENGTH
        content, sub = "", ""
        end_delimiter = list(inverse_source_code.keys())[-1]
        for ch in range(i, len(coded_content)):
            sub += coded_content[ch]
            if sub == end_delimiter:
                break
            if sub in inverse_source_code:
                content += inverse_source_code[sub]
                sub = ""
        return content
