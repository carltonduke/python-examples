
# date: 2019.09.03
# 

from flask import Flask, Response, render_template, send_file
import time


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World 3"

def get_image():
    while True:
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n'
              b'\r\n'+ img + b'\r\n')
        time.sleep(0.04) # my Firefox needs some time to display image / Chrome displays image without it
                         # 0.04s = 40ms = 25 frames per second (this can be enough)


def get_image_with_size():
    length = str(len(img)).encode() # convert to bytes
    while True:
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n'
              b'Content-Length: ' + length + b'\r\n'
              b'\r\n'+ img + b'\r\n')
        time.sleep(0.04) # my Firefox needs some time to display image / Chrome displays image without it
                         # 0.04s = 40ms = 25 frames per second (this can be enough) 

@app.route("/stream")
def stream():
    # if you use `boundary=other_name` then you have to yield `b--other_name\r\n`
    return Response(get_image_with_size(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/image")
def image():
    return send_file('test.jpg')


if(__name__ == "__main__"):
    img = open('test.jpg', 'rb').read()
    app.run(debug = True)
