from flask import Flask
from delivery.ext import site
from delivery.ext import toolbar
from delivery.ext import config

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
