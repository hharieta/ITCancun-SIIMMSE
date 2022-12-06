from marshmallow_sqlalchemy import fields
from conf import db, ma

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    control_number = db.Column(db.Integer, unique=True)
    names = db.Column(db.String(32))
    fathers_lastname = db.Column(db.String(32))
    mothers_lastname = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    passwor = db.Column(db.String(32), nullable=False)
    datebirth = db.Column(db.String(32))


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sql_session = db.session

user_schema = UserSchema()
# parameter many=True tells to UserSchema
# to expect an iterable to serialize
users_schema = UserSchema(many=True)

