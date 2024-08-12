from flask import Flask
from p3vaildev.p3vaildev.models import load_data_files
from p3vaildev.p3vaildev.config.app_conf import settings

app = Flask(__name__)
app.config['DEBUG'] = settings.app.DEBUG

# from vault.routes import *

load_data_files()
