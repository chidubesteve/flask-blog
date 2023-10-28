from flask import Flask, redirect, request, render_template, url_for, flash 
from flask_sqlalchemy import SQLAlchemy
from forms  import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)


app.config['SECRET_KEY'] = '451687de6cb7eb0d41af6d8f005decd0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///side.db'
db = SQLAlchemy(app)

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

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
       {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/") # if you want one function to be fired for multiple routes you do this
@app.route("/home") 
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# to run the app with python and not flask and all this setting

if __name__ == '__main__':
    app.run(debug=True)