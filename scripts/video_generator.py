from scripts.image_generator import ImageGenerator
from scripts.entity import Entity
from scripts.constants import *
from typing import List
from math import ceil
import cv2, os, numpy as np


class VideoGenerator(Entity):
    """
    A class to generate videos.

        Attributes
        ----------

        coded_content : str
            Text file coded content
        bit_depth : int
            Bit depth (bpp) of the image
        platform : str
            Platform to upload the video
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
        original_frames_path : str
            Path of the original frames folder
        video_frames_path : str
            Path of the video frames folder
        video_path : str
            Path of the video folder

        Methods
        -------

        fit_resolution(self) -> tuple:
            Find the best resolution for the total pixels.
        generate_images(self) -> List:
            Generate the video images (frames).
        extract_frames(self, video_path: str, output_folder: str) -> None:
            Extract the frames of the video.
        create_video(self, folder_path: str, fps: int) -> None:
            Create the video in the given format.
        save(self, file_path: str) -> None:
            Save the video in the given path.
        repeat_coded_content(self) -> str:
            Repeat the bits row of the coded content with the bit height.
        initialization(self) -> None:
            Initializate the program.
    """

    valid_kwargs = {
        "coded_content"        : str,
        "bit_depth"            : int,
        "platform"             : str,
        "bit_width"            : int,
        "bit_height"           : int,
        "original_frames_path" : str,
        "video_frames_path"    : str,
        "video_path"           : str,
    }

    def __init__(self, **kwargs: dict) -> None:
        # Validate the kwargs arguments
        self.validate_kwargs(kwargs, self.valid_kwargs)
        self.initialization()
        
    def fit_resolution(self) -> tuple:
        """
        Find the best resolution for the total pixels.

            Parameters
                None

            Returns
                return A tuple with the images dimensions, the remainder pixels and the number of frames
        """

        min_resolution, max_resolution = RESOLUTIONS[self.platform]

        # Get the dimensions of each resolution
        min_width, min_height = min_resolution
        max_width, max_height = max_resolution

        # Corner cases
        if self.total_pixels <= min_width*min_height:
            return min_resolution, 1
        elif self.total_pixels >= max_width*max_height:
            return max_resolution, ceil(self.total_pixels/(max_width*max_height))

        if max_width - min_width >= max_height - min_height:
            dimensions = []
            for width in range(min_width, max_width+1):
                height = ceil(self.total_pixels/width)
                if min_height <= height <= max_height:
                    dimensions.append(((width, height), self.total_pixels%width, ceil(self.total_pixels/(width*height))))
            best_resolution = max(dimensions, key=lambda dimension: dimension[0][0])
            return best_resolution[0], best_resolution[2]
        else:
            dimensions = []
            for height in range(min_height, max_height+1):
                width = ceil(self.total_pixels/h)
                if min_width <= width <= max_width:
                    dimensions.append(((width, height), self.total_pixels%height, ceil(self.total_pixels/(width*height))))
            best_resolution = max(dimensions, key=lambda dimension: dimension[0][0])
            return best_resolution[0], best_resolution[2]

    def generate_images(self) -> List:
        """
        Generate the video images (frames).

            Parameters
                None

            Returns
                return List with the images
        """

        coded_content_area, images = self.width*self.height*self.bit_depth, []
        for i in range(0, len(self.coded_content), coded_content_area):
            images.append(ImageGenerator(self.coded_content[i: i+coded_content_area], self.bit_depth, self.dimensions).image)
        return images

    def extract_frames(self, video_path: str, output_folder: str) -> None:
        """
        Extract the frames of the video.

            Parameters
                video_path (str): (str): Path of the video.
                output_folder (str): Path to save the video frames.

            Returns
                return List with the images
        """

        video_capture = cv2.VideoCapture(video_path)
        if not video_capture.isOpened():
            print("Error: Could not open video.")
            return
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        frame_count = 0
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            frame_filename = os.path.join(output_folder, f"frame{frame_count}.png")
            cv2.imwrite(frame_filename, frame)
            frame_count += 1
        video_capture.release()

    def create_video(self, folder_path: str, fps: int) -> None:
        """
        Create the video in the given format.

            Parameters
                folder_path (str): (str): Path to save the video
                fps (int): Number of FPS

            Returns
                return List with the images
        """

        height, width, layers = np.array(self.images[0]).shape
        # Define the codec and create VideoWriter object (H.264 codec)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for H.264 codec
        video = cv2.VideoWriter(folder_path, fourcc, fps, (width, height))
        for image in self.images:
            video.write(np.array(image))
        video.release()

    def save(self, folder_path: str) -> None:
        """
        Save the video in the given path.

            Parameters
                folder_path (str): Path to save the video

            Returns
                return None
        """

        for i in range(len(self.images)):
            self.images[i].save(folder_path+f"\\frame{i}.png")

    def repeat_coded_content(self) -> str:
        """
        Repeat the bits row of the coded content with the bit height.

            Parameters
                None

            Returns
                return Repeated coded content
        """

        row_bit_length = self.width*self.bit_depth
        repeated_coded_content = ""
        for i in range(0, len(self.coded_content), row_bit_length):
            repeated_coded_content += self.coded_content[i:i+row_bit_length]*self.bit_height
        return repeated_coded_content

    def initialization(self) -> None:
        """
        Initializate the program.

            Parameters
                None
    
            Returns
                return None
        """

        self.total_pixels = (len(self.coded_content)*self.bit_height)/self.bit_depth
        self.dimensions, self.frames = self.fit_resolution()
        self.width, self.height = self.dimensions
        self.coded_content = self.repeat_coded_content()
        print(len(self.coded_content)/self.bit_depth, self.total_pixels)
        self.images = self.generate_images()
        self.save(self.original_frames_path)
        self.create_video(self.video_path+"/output_video.mp4", 1)
        self.extract_frames(self.video_path+"/output_video.mp4", self.video_frames_path)
