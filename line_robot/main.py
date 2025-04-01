from flask import Flask, render_template, Response, request
import cv2
from gpiozero import Motor, PWMOutputDevice
from time import sleep

app = Flask(__name__)

# -----------------------------
# Motor Setup (gpiozero)
# -----------------------------
left_motor = Motor(forward=5, backward=6)
left_speed = PWMOutputDevice(13)

right_motor = Motor(forward=21, backward=26)
right_speed = PWMOutputDevice(19)

def set_speed(speed=0.5):
    left_speed.value = speed
    right_speed.value = speed

def move_forward():
    set_speed()
    left_motor.forward()
    right_motor.forward()

def move_backward():
    set_speed()
    left_motor.backward()
    right_motor.backward()

def turn_left():
    set_speed()
    left_motor.backward()
    right_motor.forward()

def turn_right():
    set_speed()
    left_motor.forward()
    right_motor.backward()

def stop():
    left_motor.stop()
    right_motor.stop()

# -----------------------------
# Camera Streaming
# -----------------------------
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

def gen_frames():
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 40]
    while True:
        success, frame = camera.read()
        if not success:
            break
        frame = cv2.resize(frame, (320, 240))  # ลดขนาดภาพ
        _, buffer = cv2.imencode('.jpg', frame, encode_param)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# -----------------------------
# Flask Routes
# -----------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    if direction == 'right':
        move_forward()
    elif direction == 'left':
        move_backward()
    elif direction == 'backward':
        turn_left()
    elif direction == 'forward':
        turn_right()
    elif direction == 'stop':
        stop()
    return ('', 204)

# -----------------------------
# Run App
# -----------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
