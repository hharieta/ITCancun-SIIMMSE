from flask import abort, make_response
from conf import db
from models.UsersModel import User, users_schema, user_schema

#####################################################
#
# FUNCTIONS CALLED BY THE OPEN API ENDPOINTS
#
#####################################################

# read all user from de data base
def read_all():
    users = User.query.all()

    return users_schema.dump(users)


# read a specific user from de data base
def read_one(control_number):
    user = User.query.filter(User.control_number == control_number).one_or_none()

    if user is not None:
        return user_schema.dump(user)
    else:
        abort(
            404, f"User with control number {control_number} not found"
        )


# create a new user. the user parameter is an object provided by the API
def create(user):
    control_number = user.get("control_number")
    existing_user = User.query.filter(User.control_number == control_number).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()

        return user_schema.dump(new_user), 201
    else:
        abort(
            406, f"User with control number {control_number} already exists"
        )


# User attributes that can be updated in the database
def update(control_number, user):
    existing_user = User.query.filter(User.control_number == control_number).one_or_none()

    if existing_user:
        update_user = user_schema.load(user, session=db.session)
        existing_user.names = update_user.names
        existing_user.fathers_lastname = update_user.fathers_lastname
        existing_user.mothers_lastname = update_user.mothers_lastname
        existing_user.email = update_user.email
        existing_user.passwor = update_user.passwor
        existing_user.datebirth = update_user.datebirth

        return user_schema.dump(existing_user), 201
    
    else:
        abort(
            404, f"User with control number {control_number} not found"
        )


def delete():
    pass
