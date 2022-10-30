from flask import Blueprint, render_template, url_for, redirect, request


views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        age = request.form.get('age')
        gender = request.form.get('gender')
        print(age)
        return redirect(url_for('emotions.home'))

    return render_template("index.html")