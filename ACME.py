from flask import Flask, request
import base64
import json
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/GetPicture",methods=['POST'])
def get_Picture():
    data = json.loads(request.data)
    base64_str = data["image"]
    image_data = base64.b64decode(base64_str)
    print(os.getcwd())
    with open('./ss.jpg','wb') as f:
        f.write(image_data)
    #img.save('haha.jpg')
    a='ok'
    return a

@app.route("/GetString",methods=['POST'])
def get_String():
    print(request.data)
    a='翻译出来的东东'
    return a
if __name__ == "__main__":
     app.run("127.0.0.1", port=80,debug=True)  #端口为8081
