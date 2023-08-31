from flask import Blueprint,jsonify,render_template,request,make_response,redirect,url_for,session
from app import db
from app.user.model import Registration
from app.super_admin.model import CreateUser
from app.admin.model import Surveyor_details
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import or_
from app.util import *
import pandas as pd
import uuid
from flask_mail import *
from config import *
from sqlalchemy import or_

user=Blueprint('user',__name__)


@user.route('/',methods=['GET','POST'])
def login():
    session.clear()
    if request.method=='POST':
        try:
            data=request.form 
            db_data=check_user(CreateUser,data.get('phone_no'))
            if check_password_hash(db_data['password1'],data.get('password')) and data.get('phone_no')==db_data['phone_no']:
                session['phone_no']=db_data.get('phone_no')
                session['name']=f"{db_data.get('first_name')} {db_data.get('last_name')}"
                session['login_time']=datetime.utcnow
                session['id']=db_data.get('id')


                    
                surveyor=check_user(Surveyor_details,db_data.get('phone_no'))
                user=check_user(Registration,db_data.get('phone_no'))

                
                if db_data['user_type']=='Surveyor':

                    if surveyor==None:
                        return redirect('admin_form')
                    else:
                        session['surveyor']=True
                        return redirect('admin_page')
                    
                if db_data['user_type']=='User':
                    session['user']=True
                    return redirect('user_home')
                


        except Exception:
            return render_template('user/login.html',msg='Incorrect Username or Password!')
    return render_template('user/login.html')



@user.route('/signup',methods=['GET','POST'])
def signup():

    if request.method=='POST':
        data=request.form.to_dict()
        admin_code=data['admin_code']
        surveyor_code=data['surveyor_code']
        data.pop('admin_code')
        data.pop('surveyor_code')
        obj=CreateUser(**data)
        hashed_password1 = generate_password_hash(data.get('password1'))
        hashed_password2 = generate_password_hash(data.get('password2'))
        obj.password1=hashed_password1
        obj.password2=hashed_password2
        try:
            id=CreateUser.query.with_entities(CreateUser.id).all()
            id_list = [i[0] for i in id]
            print(id_list)
            if data['user_type']=='User' and surveyor_code in id_list:
                uid="USR-"+surveyor_code.split('-')[-1]
                print(uid)
                obj.rid=uid
                obj.id='USR-'+str(uuid.uuid4()).split('-')[0]
            elif data['user_type']=='Surveyor' and admin_code==Config.ADMIN_CODE:
                sid='SURV-'+str(uuid.uuid4()).split('-')[0]
                obj.id=sid
                return redirect('admin_page')
            else:
                return redirect('signup')
            
            
            return redirect('/')
            

        except Exception as e:
            db.session.add(obj)
            db.session.commit()
            return redirect('/')
        

        finally:
            db.session.add(obj)
            db.session.commit()
        
       
            




    return render_template('user/signup.html')







@user.route('/create_profile',methods=['GET','POST'])
def create_profile():
    try:
        db_data=check_user(Registration,session['phone_no'])
        if db_data==None:
            return "<h2>User not registered yet.</h2>"
        else:
            if request.method=='POST':
                data=request.form.to_dict()
                # scode="SURV-"+db_data['rid'].split('-')[-1]
                # s_data=Surveyor_details.query.filter(Surveyor_details.sid==scode).first()
                # s_data=orm_object_to_dict(s_data)
                # data['uid']=db_data['id']
                # data['surveyor_name']=f"{s_data['first_name']} {s_data['last_name']}"
                # data['surveyor_code']=scode


                u_data=Registration.query.filter(Registration.uid==session['id']).first()
                u_data=orm_object_to_dict(u_data)
                data['uid']='USR-'+str(uuid.uuid4()).split('-')[0]
                data['rid']=session['id']
                data['surveyor_name']=u_data['surveyor_name']
                data['surveyor_code']=u_data['surveyor_code']
                data['no_of_members']=u_data['no_of_members']

                orm=Registration(**data)
                db.session.add(orm)
                db.session.commit()
                return redirect("user_home")

        

        
        

        return render_template('user/create_profile.html',name=session['name'])
    except Exception as e:
        print(e.args)
        return redirect('/')



@user.route('/user_home',methods=['GET','POST'])
def user_home():
    try:
        if session['user']:
            return render_template('user/user_home.html',name=session['name'])
    except:
        return redirect('/')




@user.route('/user_profile',methods=['GET','POST'])
def user_profile():
    try:
        if session['user']:
            db_data=Registration.query.filter(or_(Registration.rid==session['id'],Registration.uid==session['id'])).all()
            data = [orm_object_to_dict(item) for item in db_data]
            dd={}
            for i in data:
                for j,k in i.items():
                    if j in dd:
                        dd[j].append(k)
                    else:
                        dd[j] = [k]
            df=pd.DataFrame(data)
            df.columns=df.columns.str.replace('_',' ').str.title()

            head=df[df['Is Family Head']=='yes']
            member=df[df['Is Family Head']!='yes']
            head.drop(columns=['Is Family Head','Relation','Rid'],inplace=True)
            member.drop(columns=['Rid','Surveyor Name','Surveyor Code','No Of Members','Is Family Head'],inplace=True)
            member_to_show=head['No Of Members'].astype(int).values[0]
            member=member.head(member_to_show)
            return render_template('user/user_profile.html',head=head.to_html(classes='table table-striped'),member=member.to_html(classes='table table-striped'))
    except Exception as e:
        print(e.args)
        return "<h2>Family Not Created Yet.</h2>"


@user.route('/create_member',methods=['GET','POST'])
def create_member():
    pass

@user.route("/logout")
def logout():
    session.clear()
    return redirect('/')


