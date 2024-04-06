from scripts.image_generator import ImageGenerator
from scripts.constants import *
from typing import List
from math import ceil

class VideoGenerator:
    """
    A class to generate videos.

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
        images : List
            List with PIL Image objects

        Methods
        -------

        fit_resolution(self) -> tuple:
            Find the best resolution for the total pixels.
        generate_images(self) -> List:
            Generate the video images (frames).
        save(self, folder_path: str) -> None:
            Create the image from the pixel array.
        save(self, file_path: str) -> None:
            Save the video in the given path.
    """

    def __init__(self, coded_content: str, bit_depth: int) -> None:
        self.coded_content = coded_content
        self.bit_depth = bit_depth
        self.total_pixels = len(self.coded_content)/self.bit_depth
        self.dimensions, self.remainder, self.frames = self.fit_resolution()
        self.width, self.height = self.dimensions
        self.images = self.generate_images()

    def fit_resolution(self) -> tuple:
        """
        Find the best resolution for the total pixels.

            Parameters
                None

            Returns
                return A tuple with the images dimensions, the remainder pixels and the number of frames
        """

        dimensions, min_remainder, min_quotient = None, float("inf"), float("inf")
        for key in RESOLUTIONS:
            current_remainder = self.total_pixels%key
            if min_remainder > current_remainder:
                min_remainder = current_remainder
                min_quotient = ceil(self.total_pixels/key)
                dimensions = RESOLUTIONS[key]
        return dimensions, min_remainder, min_quotient

    def generate_images(self) -> List:
        """
        Generate the video images (frames).

            Parameters
                None

            Returns
                return List with the images
        """

        coded_content_width, images = self.width*self.height*self.bit_depth, []
        for i in range(0, len(self.coded_content), coded_content_width):
            images.append(ImageGenerator(self.coded_content[i: i+coded_content_width], self.bit_depth, self.dimensions).image)
        return images

    def save(self, folder_path: str) -> None:
        """
        Save the video in the given path.

            Parameters
                folder_path (str): Path to save the video

            Returns
                return None
        """

        for i in range(len(self.images)):
            self.images[i].save(folder_path+f"frame{i}.png")