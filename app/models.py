from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class USer(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    pitch = db.Relationship('pitch',backref = 'user', lazy = "dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(self.pass_secure,password)

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Interger, primary_key = True)
    pitch_id = db.Column(db.Interger)
    pitch_type = db.Column(db.String)
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    upvote = db.Column(db.Interger)
    downvote = db.Column(db.Interger)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls, id):
        pitch = Pitch.query.filter_by(pitch_id=id).all()
        return pitch