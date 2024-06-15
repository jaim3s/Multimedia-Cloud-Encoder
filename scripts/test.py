a = "01100"
b = ""
w = 4
h = 1
for j in range(h):
    for i in a:
        b += i*w
    b += "\n"
print(b)
b = "01001111111100000000"
c = ""
for i in range(0, len(b), w):
    cnt0, cnt1 = 0, 0
    for j in b[i:i+w]:
        if j == "0":
            cnt0 += 1
        elif j == "1":
            cnt1 += 1
    if cnt0 > cnt1:
        c += "0"
    elif cnt1 > cnt0:
        c += "1"
    else:
        c += "0"
    print(cnt0, cnt1, b[i:i+w])

print(a)
print(c)
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