from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired("Username is required"),
        Length(min=2, max=20, message='Username must be between 2 and 20 characters')
    ])
    email = StringField('Email address', validators=[
        InputRequired("Email is required"),
        Email(message='Invalid email address format')
    ])
    password = PasswordField('Password', validators=[
        InputRequired('Password is required'),
        Length(min=6, message='Password must be at least 6 characters')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        InputRequired('Please confirm your password'),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Sign Up')
    
    
class LoginForm(FlaskForm):

    email = StringField('Email address', validators=[
        InputRequired("Email is required"),
        Email(message='Invalid email address format')
    ])
    password = PasswordField('Password', validators=[
        InputRequired('Password is required'),
        Length(min=6, message='Password must be at least 6 characters')
    ])

    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')
