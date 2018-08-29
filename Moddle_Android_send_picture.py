import requests
import base64
from io import BytesIO
from PIL import Image
import json

with open("1234.jpg", "rb") as imageFile:
    base64_str = str(base64.b64encode(imageFile.read()))
g = requests.post("http://127.0.0.1:80/GetPicture", data=json.dumps({'image':base64_str}))
print(g.text)