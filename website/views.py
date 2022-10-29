from flask import Blueprint, render_template, url_for, redirect, request


views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('webcam.home'))

    return render_template("index.html")