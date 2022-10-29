from threading import Timer
from flask import Blueprint, render_template, Response
import cv2
import time

global img_counter
img_counter = 0
 
webcam = Blueprint('webcam', __name__, template_folder="./templates")
camera = cv2.VideoCapture(0)

def count(timer):
    prev = time.time()
    while timer >= 0:
        cur = time.time()
        if cur - prev >= 1:
            prev = cur 
            timer -= 1

def capture():
    global img_counter
    ret,frame = camera.read() 
    img_name = "Capture{}.png".format(img_counter)
    cv2.imwrite(img_name, cv2.flip(frame,1))
    img_counter +=1

def gen_frames():
    static_frame = None
    while True:
        success, frame = camera.read() 
        if success:
            ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
            if not static_frame:
                frame = buffer.tobytes()
            else:
                frame = static_frame 

            # ------ problem ------- #
            #if count(3):
             #   capture()
              #  static_frame = frame

            # Issue: webcam stops working the frame just becomes a static frame
            # Goal: Webcam works for 3 secs then becomes a static image when the image is captured  

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@webcam.route('/')
def home():
    return render_template('camera.html')

# Generates a Response so that html can use it as a img src
@webcam.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame') # "multipart/x-mixed-replace" response type that expects multiple frames

camera.release()
cv2.destroyAllWindows()