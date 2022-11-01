from os import remove
from flask import Blueprint, redirect, render_template, url_for
import random
from .camera import count

angry = "angry.html"
disgust = "disgust.html"
fear = "fear.html"
happy = "happy.html"
neutral = "neutral.html"
sad = "sad.html"
suprised = "suprised.html"

emotions = Blueprint('emotions', __name__, template_folder='./templates/emotion_templates')

Emotion = [angry,disgust,fear,happy,neutral,sad,suprised]

global AngryCount, DisgustCount, FearCount, HappyCount, NeutralCount, SadCount, SuprisedCount
AngryCount = 0
DisgustCount = 0
FearCount = 0
HappyCount = 0
NeutralCount = 0
SadCount = 0
SuprisedCount = 0

@emotions.route('/', methods=['GET'])
def home():
    global AngryCount, DisgustCount, FearCount, HappyCount, NeutralCount, SadCount, SuprisedCount

    RandomEmotion = random.choice(Emotion)

    if RandomEmotion == angry:
        if AngryCount <= 1:
            AngryCount += 1
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}
            
        else:
            Emotion.remove(angry)
            RandomEmotion = random.choice(Emotion)
            print(Emotion)
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}

    if RandomEmotion == disgust:
        if DisgustCount <= 1:
            DisgustCount += 1
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}
        else:
            Emotion.remove(disgust)
            RandomEmotion = random.choice(Emotion)
            print(Emotion)
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}

    if RandomEmotion == fear:
        if FearCount <= 1:
            FearCount += 1
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}
        else:
            Emotion.remove(fear)
            RandomEmotion = random.choice(Emotion)
            print(Emotion)
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}

    if RandomEmotion == happy:
        if HappyCount <= 1:
            HappyCount += 1
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}
        else:
            Emotion.remove(happy)
            RandomEmotion = random.choice(Emotion)
            print(Emotion)
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}

    if RandomEmotion == neutral:
        if NeutralCount <= 1:
            NeutralCount += 1
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}
        else:
            Emotion.remove(neutral)
            RandomEmotion = random.choice(Emotion)
            print(Emotion)
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}

    if RandomEmotion == sad:
        if SadCount <= 1:
            SadCount += 1
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}
        else:
            Emotion.remove(sad)
            RandomEmotion = random.choice(Emotion)
            print(Emotion)
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}

    if RandomEmotion == suprised:
        if SuprisedCount <= 1:
            SuprisedCount += 1
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}
        else:
            Emotion.remove(suprised)
            RandomEmotion = random.choice(Emotion)
            print(Emotion)
            return render_template(RandomEmotion), {"Refresh": "3; url=http://127.0.0.1:5000/webcam/"}
