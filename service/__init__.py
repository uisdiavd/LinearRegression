# Trying to set logging level, have not been able to define object 'app' for use with config.from_object(config)
from flask import Flask
from service import config

app = Flask(__name__)

app.config.from_object(config)

from service import models

