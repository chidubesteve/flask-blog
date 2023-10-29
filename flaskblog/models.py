from flaskblog import db
from datetime import datetime

# class/module to hold our users
class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # we can set maybe a rooms attribute as a relationship between the user and the booked room
    posts = db.relationship('Post', backref='author', lazy=True)
    # this backref helps us target the user who made a particular post(by giving us access to more info that was not specified) and the lazy attribute is for lazy loading
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
# we can use this for rooms
#  we can change in to include data like, name of the room, the image of the room, the price of the room, a short description of the room, and maybe a boolean keeping track of whether it's booked or not and maybe a longer detail of the room... and any other thing you wish to add
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # we will be using the id of the user as a FK in this column to reference each post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"