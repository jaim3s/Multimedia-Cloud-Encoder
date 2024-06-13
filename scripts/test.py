import cv2
import os

def create_video_from_images(image_folder, output_video, fps):
    # Get the list of images
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort()  # Sort the images by name (assuming they are named sequentially)

    # Read the first image to get the dimensions
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'XVID' or 'MJPG' as well
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)
        video.write(frame)

    # Release the video writer object
    video.release()

if __name__ == "__main__":
    image_folder = 'C:/Users/ophys/OneDrive/Documents/UN/8 semester/Codification theory/Project/frame_imgs'
    output_video = 'output_video.mp4'
    fps = 24  # Frames per second

    create_video_from_images(image_folder, output_video, fps)


"""
from PIL import Image
import io

def log(content: str) -> None:
        with open(log_path, "w") as file:
            file.write(content)

# Example usage:
image_path = "C://Users//ophys//OneDrive//Documents//UN//8 semester//Codification theory//Project//imgs//mario.png"
log_path = "C://Users//ophys//OneDrive//Documents//UN//8 semester//Codification theory//Project//log.txt"

# This portion is part of my test code
byteImgIO = io.BytesIO()
byteImg = Image.open(image_path)
byteImg.save(byteImgIO, "PNG")
byteImgIO.seek(0)
byteImg = byteImgIO.read()
log(str(byteImg))

# Non test code
dataBytesIO = io.BytesIO(byteImg)
test = Image.open(dataBytesIO)
test.show()

print(image_path[image_path.rfind(".")+1:])
"""