import requests

strffgfdr="111"

g = requests.post("http://127.0.0.1:80/GetString", data=strffgfdr)
print(g.text)