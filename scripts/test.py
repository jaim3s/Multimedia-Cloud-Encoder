import cv2
import os
def extract_frames(video_path, output_folder):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    # Check if video opened successfully
    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return

    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0
    while True:
        # Read the next frame
        ret, frame = video_capture.read()
        
        # If there are no more frames, break the loop
        if not ret:
            break
        
        # Save the frame as an image file
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        
        # Print progress
        print(f"Extracted frame {frame_count}")
        
        frame_count += 1

    # Release the video capture object
    video_capture.release()
    print("All frames extracted.")

# Example usage
video_path = 'C:/Users/ophys/OneDrive/Documents/UN/8 semester/Codification theory/Project/videos/output_video.avi'
output_folder = 'C:/Users/ophys/OneDrive/Documents/UN/8 semester/Codification theory/Project/video_frames'
extract_frames(video_path, output_folder)

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