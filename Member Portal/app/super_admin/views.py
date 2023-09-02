from flask import Blueprint,jsonify,render_template,request,make_response,redirect,url_for,session
from app import db
from app.super_admin.model import CreateUser,LoginDetails
from app.user.model import Registration
from app.admin.model import Surveyor_details
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app.util import *
import pandas as pd
from config import Config



super_admin=Blueprint('super_admin',__name__)


@super_admin.route('/super_admin_home')
def super_admin_home():
    try:
        if session['super_admin']:
            return render_template('super_admin/super_admin_home.html')
    except:
        return redirect('/')



@super_admin.route('/login',methods=['GET','POST'])
def super_admin_login():
    if request.method=='POST':
        data=request.form
        if data.get('admin_key')==Config.SUPER_ADMIN_KEY and data.get('password')==Config.SUPER_ADMIN_PASSWORD:
            session['super_admin']=True
            return redirect('/super_admin_home')
        else:
            pass
    return render_template('super_admin/login.html')


@super_admin.route('/all_admin',methods=['GET','POST'])
def all_admin():
    try:
        if session['super_admin']:
            try:
                db_data=Surveyor_details.query.all()
                data=query_all(db_data,Surveyor_details)
                columns=[str(x).replace('_',' ').title() for x in data.keys()]
                df=pd.DataFrame(data)
                df.sort_values(by=['phone_no'],inplace=True)
                df.columns=columns
                # print(df)
                return render_template('super_admin/all_user.html',df=df)
            except:
                return "<h2>No Surveyor has been created yet.</h2>"
    
    except:
        return redirect('/')


@super_admin.route('/all_user/<string:id>',methods=['GET','POST'])
def all_user(id):
    try:
        if session['super_admin']:
            try:
                
                
                if request.method=="GET":
                    db_data=Registration.query.filter(Registration.surveyor_code==id).all()
                    data=query_all(db_data,Registration)
                    columns=[str(x).replace('_',' ').title() for x in data.keys()]
                    df=pd.DataFrame(data)
                    df.sort_values(by=['phone_no'],inplace=True)
                    df.columns=columns
                    return render_template('super_admin/all_subuser.html',df=df.to_html(classes='table table-striped'))

            


            except:
                return "<h2>This Surveyor have not created any user yet.</h2>"
    
    except:
        return redirect('/')



@super_admin.route('/',methods=['GET','POST'])
def logout():
    session.clear()
    return redirect('/')