from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

# Initializing application
def create_app(config_name):

    app = Flask(__name__)


    # Setting up configuration
    app.config.from_object(config_options[config_name])
     
     #setting up flask extensions
    bootstrap.init_app(app) 

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #setting config
    from .request import manage_requests
    manage_requests(app)


    return app