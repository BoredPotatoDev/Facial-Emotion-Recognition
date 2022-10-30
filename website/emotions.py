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

@emotions.route('/')
def home():
    global change

    if change == False:
        RandomEmotion = random.choice([angry,disgust,fear,happy,neutral,sad,suprised])
        return render_template(RandomEmotion)
    else:
        return redirect(url_for('webcam.main'))