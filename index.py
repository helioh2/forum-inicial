import datetime
import json
from time import strptime
from typing import List
from flask import (
    Flask,
    session,
    escape,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_sqlalchemy import Pagination, SQLAlchemy


from model import Usuario, db

from flask_migrate import Migrate

from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/forum'

db.init_app(app)
migrate = Migrate(app, db)

PER_PAGE = 10

@app.get("/")
def home():
    return "OLÁ FORUM"



