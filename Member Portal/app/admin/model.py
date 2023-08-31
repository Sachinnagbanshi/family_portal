from app import db
from datetime import datetime



class Surveyor_details(db.Model):
    __tablename__ = 'surveyor_details'

    sid = db.Column(db.String(20),db.ForeignKey('user_master.id'),unique=True,primary_key=True)
    first_name =db.Column(db.String(100), nullable=False)
    last_name =db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=True)
    aadhar_no = db.Column(db.String(16),unique=True, nullable=False)
    pan = db.Column(db.String(10),unique=True ,nullable=False)
    voter_id = db.Column(db.String(20),unique=True, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    pin = db.Column(db.String(10), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    address_line_1 = db.Column(db.String(200), nullable=False)
    address_line_2 = db.Column(db.String(200))
    qualification = db.Column(db.String(20),nullable=False)
    joining_date = db.Column(db.Date,default=datetime.utcnow,nullable=False)
    
    user_details=db.relationship("Registration", backref="surveyor_details",lazy=True)