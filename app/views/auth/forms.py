from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import EqualTo, DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=3, max=50)])
    password1 = PasswordField(label="Password", validators=[DataRequired(), Length(min=6, max=50)])
    password2 = PasswordField(label="Confirm Password", validators=[DataRequired(), Length(min=6, max=50), EqualTo(password1)])
    

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Stay logged in", validators=[])
