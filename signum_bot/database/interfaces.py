from signum_bot.database.connection import db
from pymongo.collection import Collection

"""
    User
    username: str = None
    honor: int = None
    languages: dict = None
    total_completed: int = None
"""


# def add_student(username):
#    return connect.db.student.insert_one(username)
#
#
# def add_teacher(username):
#    return connect.db.teacher.insert_one(username)
#
#
# def add_admin(tg_id):
#    return connect.db.admin.insert_one(tg_id)

# Todo: Posmotret kak rabotat s mongodb v Python
# Todo: Posmotret kak delat indixaziu polei v mongodb
# todo dobavit v argument tg_id
def update_username(username: str, new_data: dict, collection: Collection):
    #  changed = {'username': f'{username}'}
    return db.collection.update_one({'username': f'{username}'}, new_data)


def update_user_tg_id(tg_id: int, new_data: dict, collection: Collection):
    #   changed = {'tg_id': f'{tg_id}'}
    return db.collection.update_one({'tg_id': f'{tg_id}'}, new_data)


def delete_user(tg_id: int, username: str, collection: Collection):
    # deleted = {'username': f'{username}','tg_id': f'{tg_id}'}
    return db.collection.delete({'username': f'{username}', 'tg_id': f'{tg_id}'})


def create_user(tg_id: int, username: str, collection: Collection):
    return db.collection.insert_one(tg_id, username)


def get_user(tg_id: int, username: str, collection: Collection):
    return db.collection.find_one({'username': f'{username}', 'tg_id': f'{tg_id}'})
