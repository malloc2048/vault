from flask import Flask
from vault.models import load_data_files
from vault.config.app_conf import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)

from vault.routes import *

load_data_files()
