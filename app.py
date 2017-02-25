from flask import Flask, render_template, Response, redirect, url_for
import cv2
from camera import Camera

cam1 = Camera(0)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    global recorder
    while True:
        
        frame = camera.get_frame()

        frame = cv2.resize(frame, (384, 216))

        sucess, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 30])

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


@app.route('/front_feed')
def front_feed():
    return Response(gen(cam1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/back_feed')
def back_feed():
    return Response(gen(cam1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)
