import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://wallpaperaccess.com/full/284755.jpg")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

path = "./image." + image.format

print(image.size, image.format, image.mode)

try:
    image.save(path, image.format)
except IOError:
    print("Can't save image!")