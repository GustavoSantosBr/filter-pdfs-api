from flask import Flask
from flask_cors import CORS

from src.Application import Routes, blueprint_file
from src.Application.Handler.PostFileHandler import PostFileHandler


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(blueprint_file)
    CORS(app)
    return app
