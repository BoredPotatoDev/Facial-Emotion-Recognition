from flask import Blueprint, redirect, render_template, url_for
import random
from .camera import count

global change
change = False

angry = "angry.html"
disgust = "disgust.html"
fear = "fear.html"
happy = "happy.html"
neutral = "neutral.html"
sad = "sad.html"
suprised = "suprised.html"

emotions = Blueprint('emotions', __name__)

@emotions.route('/', methods=['GET'])
def home():
    RandomEmotion = random.choice([angry,disgust,fear,happy,neutral,sad,suprised])
    return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}
