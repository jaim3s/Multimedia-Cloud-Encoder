import numpy as np
import scripts.constants, os
from PIL import Image
from typing import List
import matplotlib.pyplot as plt

class ImageComparator:

    def __init__(self, original_frames_path: str, video_frames_path: str, comparison_path: str) -> None:
        self.original_frames_path = original_frames_path
        self.video_frames_path = video_frames_path
        self.comparison_path = comparison_path
        self.comparisons = self.compare() 
        self.save(self.comparisons)

    def rgb_distance(self, color1: np.ndarray, color2: np.ndarray) -> float:
        """
        Calculate the distance between two RGB colors.

            Parameters
                color1 (np.ndarray): Fist RGB color
                color2 (np.ndarray): Second RGB color

            Returns
                return The distance between both colors
        """

        color1, color2 = np.array(color1, dtype=int), np.array(color2, dtype=int)
        return np.sum(np.square(color2 - color1))

    def rgb_similarity(self, color1: np.ndarray, color2: np.ndarray) -> float:
        """
        Calculate the similarity between two RGB colors.

            Parameters
                color1 (np.ndarray): Fist RGB color
                color2 (np.ndarray): Second RGB color

            Returns
                return The similarity between two colors (between [0, 1])
        """

        return ((scripts.constants.MAX_DIST - self.rgb_distance(color1, color2)) / scripts.constants.MAX_DIST)

    def save(self, comparisons: List[np.ndarray]) -> None:
        """
        Save the comparisons matrix. 

            Parameters
                None
    
            Returns
                return None
        """

        for i in range(len(comparisons)):
            plt.figure(figsize=(6, 4))
            plt.imshow(comparisons[i], cmap="viridis", interpolation="nearest")

            # Add color bar indicating the scale
            plt.colorbar()

            # Optional: Add labels, title, etc.
            plt.title(f"Original frame{i} vs Video frame{i}")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")

            # Show plot
            plt.savefig(self.comparison_path + f"\\cmp_frame{i}.png", dpi=300)

    def average(self, comparisons: List[np.ndarray]) -> float:
        pass

    def compare(self) -> List[np.ndarray]:
        """
        Compare two images. 

            Parameters
                None
    
            Returns
                return None
        """
        
        # Iterate over all files in the directory
        comparisons = []
        for filename in os.listdir(self.original_frames_path):
            original_file_path = os.path.join(self.original_frames_path, filename)
            video_file_path = os.path.join(self.video_frames_path, filename)
            if os.path.isfile(original_file_path) and os.path.isfile(video_file_path):
                original_img = Image.open(original_file_path)
                video_img = Image.open(video_file_path)
                width, height = original_img.size
                comparison = np.zeros(shape=(height, width), dtype=np.float64)
                for y in range(height):
                    for x in range(width):
                        pixel0 = original_img.getpixel((x, y))
                        pixel1 = video_img.getpixel((x, y))
                        comparison[y][x] = self.rgb_similarity(pixel1, pixel0)
                comparisons.append(comparison)
        return comparisons




