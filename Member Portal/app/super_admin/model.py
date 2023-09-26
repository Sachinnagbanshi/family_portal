from app import db
from datetime import datetime
from app.admin.model import Surveyor_details
from app.user.model import Registration

class CreateUser(db.Model):
    __tablename__='user_master'
    id=db.Column(db.String(20),primary_key=True,nullable=False)
    rid=db.Column(db.String(20),nullable=True)
    user_type=db.Column(db.String(20), nullable=False)
    first_name=db.Column(db.String(20),nullable=False)
    last_name=db.Column(db.String(20),nullable=False)
    phone_no=db.Column(db.String(20),unique=True,nullable=False)
    password1=db.Column(db.String(200),nullable=False)
    password2=db.Column(db.String(200),nullable=False)
    date=db.Column(db.DateTime,default=datetime.utcnow)

    surveyor_details = db.relationship("Surveyor_details", backref="user_master",lazy=True)
    registration = db.relationship("Registration", backref="user_master",lazy=True)
    



class LoginDetails(db.Model):
    __tablename__='session_details'
    session_id=db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    login_time=db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    logout_time=db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    user=db.Column(db.String,nullable=False)