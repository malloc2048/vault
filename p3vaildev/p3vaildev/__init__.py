from flask import Flask
from p3vaildev.config.app_conf import settings

app = Flask(__name__)
app.config['DEBUG'] = settings.debug

from p3vaildev.routes import *
