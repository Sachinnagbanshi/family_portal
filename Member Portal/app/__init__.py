from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app=Flask(__name__)

CORS(app)

app.config.from_object('config.Config')

db=SQLAlchemy(app)
Session(app)

from app.user.views import user
from app.admin.views import admin
from app.super_admin.views import super_admin

app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(super_admin)