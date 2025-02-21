from flask import Flask
from vault.models import load_data_files
from vault.config.app_conf import settings

# TODO add a database and auth
#  https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

app = Flask(__name__)
app.config['DEBUG'] = settings.app.DEBUG

from vault.routes import *

load_data_files()
