from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'testapp'

    from .views import views
    from .camera import webcam
    from .emotions import emotions

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(webcam, url_prefix='/webcam/')
    app.register_blueprint(emotions, url_prefix='/emotions/')

    return app
