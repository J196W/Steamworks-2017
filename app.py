from flask import Flask, render_template, Response, redirect, url_for
import cv2
from record import Record

recorder = Record()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def gen(num):
    global recorder
    while True:

        frame = recorder.get_curr_frame(num)

        frame = cv2.resize(frame, (640, 360))

        sucess, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 30])

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')


@app.route('/front_feed')
def front_feed():
    return Response(gen(1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/back_feed')
def back_feed():
    return Response(gen(2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera_process_change')
def camera_process_change():
    global recorder
    recorder.end()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='localhost', debug=False, port=80)
