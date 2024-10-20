from flask import Flask


app = Flask(__name__)

import app.calc as calc

from app import routes