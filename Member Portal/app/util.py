from app import db



def orm_object_to_dict(orm_object):
    return {c.name: getattr(orm_object, c.name) for c in orm_object.__table__.columns}



def check_user(orm,key):
    try:
        db_data=orm.query.filter(orm.phone_no==key).first()
        db_data=orm_object_to_dict(db_data)
    except:
        db_data=None
    return db_data



def query_all(all_users,orm):

    users_dict = {}

    for user in all_users:
        for column in orm.__table__.columns:
            column_name = column.name
            if column_name not in users_dict:
                users_dict[column_name] = []
            users_dict[column_name].append(getattr(user, column_name))

    return users_dict




def download_file(orm):
    import pandas as pd
    from io import BytesIO
    data=orm.query.filter().all()
    data=query_all(data,orm)
    columns=[str(x).replace('_',' ').title() for x in data.keys()]
    df=pd.DataFrame(data)
    df.columns=columns
    excel_buffer = BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='openpyxl') as excel_writer:
        df.to_excel(excel_writer, index=False)
    
    excel_buffer.seek(0)

    return excel_buffer