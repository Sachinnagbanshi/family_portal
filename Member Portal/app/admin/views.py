from flask import Blueprint,jsonify,render_template,request,make_response,redirect,url_for,session
from app import db
from app.util import *
from app.user.model import Registration
from app.admin.model import Surveyor_details
from app.super_admin.model import CreateUser
from datetime import datetime
import pandas as pd
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/admin_form',methods=['GET','POST'])
def admin_form():
    
    if request.method=='POST':
        data=request.form.to_dict()
        db_data=check_user(CreateUser,session['phone_no'])
        data['sid']=db_data['id']
        data['first_name']=db_data['first_name']
        data['last_name']=db_data['last_name']
        data['phone_no']=db_data['phone_no']
        obj=Surveyor_details(**data)
        db.session.add(obj)
        db.session.commit()
        return redirect('admin_page')
    return render_template('admin/admin_form.html')


   

@admin.route('/admin_page')
def admin_page():
    try:
        if session['surveyor']:
            return render_template('admin/admin_home.html',name=session['name'])
    except Exception as e:
        print(e.args)
        return redirect('/')

@admin.route('/user_report')
def user_report():
    try:
        try:
            if session['surveyor']:
                db_data=check_user(CreateUser,session['phone_no'])
                scode="SURV-"+db_data['id'].split('-')[-1]
                u_data=Registration.query.filter(Registration.surveyor_code==scode).all()
                data=query_all(u_data,Registration)
                columns=[str(x).replace('_',' ').title() for x in data.keys()]
                df=pd.DataFrame(data)
                df.sort_values(by=['phone_no'],inplace=True)
                df.columns=columns
                df.drop(columns=['Surveyor Name','Surveyor Code'],inplace=True)
                return render_template('admin/view_users.html',df=df.to_html(classes='table table-striped'))
        except:
            return "<h1>No Family is created.</h2>"

    except Exception as e:
        print(e.args)
        return redirect('/')
     


@admin.route('/create_family',methods=['GET','POST'])
def create_family():

    try:
        if session['surveyor']:
            
            try:
                if request.method=='POST':
                    data=request.form.to_dict()
                    user_data=check_user(CreateUser,data['phone_no'])
                    id=session['id'].replace('SURV-','')
                    if id not in user_data['rid']:
                        return "<h2>You Cannot Create this User</h2>"
                        
                    else:
                        if type(user_data)==dict:
                            scode="SURV-"+user_data['rid'].split('-')[-1]
                            s_data=Surveyor_details.query.filter(Surveyor_details.sid==scode).first()
                            s_data=orm_object_to_dict(s_data)
                            data['uid']=user_data['id']
                            data['first_name']=user_data['first_name']
                            data['last_name']=user_data['last_name']
                            data['phone_no']=user_data['phone_no']
                            data['surveyor_name']=f"{s_data['first_name']} {s_data['last_name']}"
                            data['surveyor_code']=scode
                            orm=Registration(**data)
                            db.session.add(orm)
                            db.session.commit()
                            return redirect("admin_page")
                        else:
                            return "User Not Created Yet!"

        
            except Exception as e:
                print("User Not Created",e.args)
                return redirect('create_family')





                    # orm=Registration(**data)
                    # id='SURV-'+str(uuid.uuid4()).split('-')[0]
                    # orm.uid=id
                    # db.session.add(orm)
                    # db.session.commit()
                    # session['family_created']=True
                    # db_data=Registration.query().all()
                    # all_data=query_all(db_data,Registration)
                    # session['no_of_family_created']=len(set(all_data['uid']))


            return render_template('admin/create_family.html')
    except Exception as e:
        print(e.args)
        return redirect('/')



@admin.route('/')
def logout():
    session.clear()
    return redirect('/')