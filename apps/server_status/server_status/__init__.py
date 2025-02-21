from flask import Flask
from server_status.config.app_conf import settings

app = Flask(__name__)
app.config['DEBUG'] = settings.debug

from server_status.routes import *
