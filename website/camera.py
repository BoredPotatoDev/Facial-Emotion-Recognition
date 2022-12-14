from flask import Blueprint, redirect, render_template, Response, url_for
import cv2
import time

from website.webcam import VideoCamera

global img_counter, taken
taken = True
img_counter = 0
 
webcam = Blueprint('webcam', __name__, template_folder="./templates")
camera = cv2.VideoCapture(0)

def count(TIMER):
    prev = time.time()
    while TIMER >= 0:
        cur = time.time()
        if cur - prev >= 1:
            prev = cur 
            TIMER -= 1

def capture():
    cam = cv2.VideoCapture(0)
    global img_counter
    ret,frame = cam.read() 
    img_name = f"Capture{img_counter}.png"
    cv2.imwrite(img_name, cv2.flip(frame,1))
    print("{} written!".format(img_name))
    img_counter +=1


def gen(camera):
    while True:
        data= camera.get_frame()
        
        frame=data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@webcam.route('/')
def main():
    return render_template('camera.html'), {"Refresh": "5; url=http://127.0.0.1:5000/emotions/"}


# Generates a Response so that html can use it as a img src
@webcam.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame') # "multipart/x-mixed-replace" response type that expects multiple frames

camera.release()
cv2.destroyAllWindows()