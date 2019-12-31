from flask import Flask
from config import config


def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
	

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.after_request(after_request)
    return app
