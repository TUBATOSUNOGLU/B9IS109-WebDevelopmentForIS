from flask_wtf import FlaskForm
from flaskblog.models import User
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)


class Registrationform(FlaskForm):
    username=StringField('Username', 
                         validators=[DataRequired(), Length(min=2, max=20)])
    email=StringField('Email', 
                      validators=[DataRequired(), Email()])
    password=PasswordField('Password', 
                           validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',
                                   validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose a different one')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken, please choose a different one')
    
        
class Loginform(FlaskForm):
    email=StringField('Email', 
                      validators=[DataRequired(), Email()])
    password=PasswordField('Password', 
                           validators=[DataRequired()])
    remember=BooleanField('Remember')
    submit=SubmitField('Login')