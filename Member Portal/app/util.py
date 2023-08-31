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
