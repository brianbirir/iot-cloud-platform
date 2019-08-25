from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from werkzeug.debug import DebuggedApplication

from src.model import db
from src.user import User
from src.test import TestApi
from src.auth import Login, Logout
from src.device import Device
from src.project import Project


def create_app(config_object='config.DevelopmentConfig'):
    """
    :param config_object:
    :return: src

    This factory returns the initialized Flask app

    """
    app = Flask(__name__)
    app.config.from_object(config_object)  # load configurations object

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    # database initialization
    db.init_app(app)
    migrate = Migrate(app, db)

    # resource routing
    api = Api(app)
    api.add_resource(User, '/api/user', '/api/user/<int:user_id>')
    api.add_resource(Login, '/api/login')
    api.add_resource(Logout, '/api/logout')
    api.add_resource(TestApi, '/api/test')
    api.add_resource(Device, '/api/device')
    api.add_resource(Project, '/api/project')

    return app
