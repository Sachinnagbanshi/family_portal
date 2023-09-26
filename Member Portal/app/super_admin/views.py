from flask import Blueprint,jsonify,render_template,request,make_response,redirect,url_for,session,send_file,Response
from app import db
from app.super_admin.model import CreateUser,LoginDetails
from app.user.model import Registration
from app.admin.model import Surveyor_details
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app.util import *
import pandas as pd
from config import Config

#postgres://member_portal_user:2NYQFWKRODcHVbJyCtgt530HZpZttigI@dpg-ck97gk6gtj9c73ak5jr0-a.oregon-postgres.render.com/member_portal




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
                    db_data=Registration.query.filter(Registration.surveyor_code==id,Registration.is_family_head=='yes').all()
                    data=query_all(db_data,Registration)
                    columns=[str(x).replace('_',' ').title() for x in data.keys()]
                    df=pd.DataFrame(data)
                    df.sort_values(by=['phone_no'],inplace=True)
                    df.columns=columns
                    return render_template('super_admin/all_head.html',df=df)

            


            except Exception as e:
                # print(e.args)
                return "<h2>This Surveyor have not created any family head yet.</h2>"
    
    except:
        return redirect('/')


@super_admin.route('/all_subuser/<string:id>',methods=['GET','POST'])
def all_subuser(id):
    try:
        if session['super_admin']:
            try:
                
                if request.method=="GET":
                    db_data=Registration.query.filter(Registration.rid==id).all()
                    data=query_all(db_data,Registration)
                    columns=[str(x).replace('_',' ').title() for x in data.keys()]
                    df=pd.DataFrame(data)
                    df.sort_values(by=['phone_no'],inplace=True)
                    df.columns=columns
                    df.drop(columns=['Surveyor Name','No Of Members','Is Family Head'],inplace=True)
                    return render_template('super_admin/all_subuser.html',df=df)

            


            except Exception as e:
                print(e.args)
                return "<h2>This Surveyor have not created any family head yet.</h2>"
    
    except:
        return redirect('/')


@super_admin.route('/download_data_surveyor',methods=['GET','POST'])
def download_data_surveyor():
    try:
        if session['super_admin']:
            excel_buffer=download_file(Surveyor_details)
            response = Response(excel_buffer.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response.headers['Content-Disposition'] = 'attachment; filename=surveyor_details.xlsx'
    
            return response
    except Exception as e:
        print(e.args)
        return redirect('/')


@super_admin.route('/download_data_family',methods=['GET','POST'])
def download_data_family():
    try:
        if session['super_admin']:
            excel_buffer=download_file(Registration)
            response = Response(excel_buffer.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response.headers['Content-Disposition'] = 'attachment; filename=family_details.xlsx'
    
            return response
    except Exception as e:
        print(e.args)
        return redirect('/')


@super_admin.route('/',methods=['GET','POST'])
def logout():
    session.clear()
    return redirect('/')