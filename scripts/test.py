from math import log

print(log(8, 2))

"""
from PIL import Image
import io

def log(content: str) -> None:
        with open(log_path, "w") as file:
            file.write(content)

# Example usage:
image_path = "C:\\Users\\ophys\\OneDrive\\Documents\\UN\\8 semester\\Codification theory\\Project\\imgs\\mario.png"
log_path = "C:\\Users\\ophys\\OneDrive\\Documents\\UN\\8 semester\\Codification theory\\Project\\log.txt"

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