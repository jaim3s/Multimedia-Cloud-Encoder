from scripts.constants import *
from scripts.misc import *
from typing import List
from PIL import Image

class ImageGenerator:
    """
    A class to generate images.

        Attributes
        ----------

        coded_content : str
            Text file coded content
        bit_depth : int
            Bit depth (bpp) of the image
        total_pixels : float
            Total number of pixels to use in the image
        dimensions : tuple 
            Dimensions (width and height) of the image
        width : int
            Width of the image
        height : int
            Height of the image
        pixel_array : List[List]
            Matrix with pixels
        image : "PIL.Image.Image"
            PIL Image object

        Methods
        -------

        generate_pixels(self) -> List:
            Generate the image pixels from the content.
        get_pixel_array(self, pixels: List) -> List[List]:
            Generate the array of pixels from the pixel list.
        create_img(self) -> "PIL.Image.Image":
            Create the image from the pixel array.
        save(self, file_path: str) -> None:
            Save the image in the given path.
    """

    def __init__(self, coded_content: str, bit_depth: int, dimensions: tuple) -> None:
        self.coded_content = coded_content
        self.bit_depth = bit_depth
        self.total_pixels = len(self.coded_content)/self.bit_depth
        self.dimensions = dimensions
        self.width, self.height = self.dimensions
        self.pixel_array = self.get_pixel_array(self.generate_pixels())
        self.image = self.create_img()

    def generate_pixels(self) -> List:
        """
        Generate the image pixels from the content.

            Parameters
                None

            Returns
                return The list of pixels
        """

        pixels = []
        for i in range(0, len(self.coded_content), self.bit_depth):
            splitted_coded_content, sub = self.coded_content[i:i+self.bit_depth], []
            # Divide by the number of channels
            for j in range(0, len(splitted_coded_content), self.bit_depth//3):
                if splitted_coded_content[j:j+self.bit_depth//3]:
                    if len(splitted_coded_content[j:j+8]) < 8:
                        sub.append(int(zero_pad_right(splitted_coded_content[j:j+8], self.bit_depth//3), 2))
                    else:
                        sub.append(int(splitted_coded_content[j:j+8], 2))
            if len(sub) < 3:
                for i in range(3-len(sub)):
                    sub.append(0)
            pixels.append(tuple(sub))
        return pixels

    def get_pixel_array(self, pixels: List) -> List[List]:
        """
        Generate the array of pixels from the pixel list.

            Parameters
                pixels (List): List of pixels

            Returns
                return The array of pixels
        """

        array = []
        for i in range(self.height): 
            array.append(pixels[i*self.width:(i+1)*self.width])
        if len(array[-1]) < self.width:
            for i in range(self.width-len(array[-1])):
                array[-1].append(tuple([0, 0, 0]))
        return array

    def create_img(self) -> "PIL.Image.Image":
        """
        Create the image from the pixel array.

            Parameters
                None

            Returns
                return PIL.Image.Image create from the the pixel array
        """

        image = Image.new(MODES[self.bit_depth], (self.width, self.height))
        for row in range(len(self.pixel_array)):
            for col in range(len(self.pixel_array[row])):
                pixel_value = self.pixel_array[row][col]
                image.putpixel((col, row), pixel_value)
        return image

    def save(self, file_path: str) -> None:
        """
        Save the image in the given path.

            Parameters
                file_path (str): Path to save the image

            Returns
                return None
        """

        self.image.save(file_path)