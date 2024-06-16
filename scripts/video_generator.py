from scripts.image_generator import ImageGenerator
from scripts.constants import *
from typing import List
from math import ceil
import numpy as np
import cv2, os

class VideoGenerator:
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
    """

    def __init__(self, coded_content: str, bit_depth: int, platform: str, original_frames_path: str, video_frames_path: str, video_path: str) -> None:
        self.coded_content = coded_content
        self.bit_depth = bit_depth
        self.platform = platform
        self.total_pixels = len(self.coded_content)/self.bit_depth
        self.dimensions, self.frames = self.fit_resolution()
        self.width, self.height = self.dimensions
        self.images = self.generate_images()
        self.save(original_frames_path)
        self.create_video(video_path+"/output_video.mp4", 1)
        self.extract_frames(video_path+"/output_video.mp4", video_frames_path)

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
        min_w, min_h = min_resolution
        max_w, max_h = max_resolution

        # Corner cases
        if self.total_pixels <= min_w*min_h:
            return min_resolution, 1
        elif self.total_pixels >= max_w*max_h:
            return max_resolution, ceil(self.total_pixels/(max_w*max_h))

        if max_w - min_w >= max_h - min_h:
            dimensions = []
            for w in range(min_w, max_w+1):
                if min_h <= ceil(self.total_pixels/w) <= max_h:
                    dimensions.append(((w, ceil(self.total_pixels/w)), self.total_pixels%w, ceil(self.total_pixels/w)))
            best_resolution = min(dimensions, key=lambda dimension: dimension[1])
            return best_resolution[0], best_resolution[2]
        else:
            dimensions = []
            for h in range(min_h, max_h+1):
                if min_w <= ceil(self.total_pixels/h) <= max_w:
                    dimensions.append(((ceil(self.total_pixels/h), h), self.total_pixels%h, ceil(self.total_pixels/h)))
            best_resolution = min(dimensions, key=lambda dimension: dimension[1])
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