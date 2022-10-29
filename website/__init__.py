from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'testapp'

    from .views import views
    from .camera import webcam

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(webcam, url_prefix='/webcam')

    return app
