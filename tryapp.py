from wtforms import Form,StringField,RadioField, PasswordField, IntegerField,SubmitField, TextAreaField
from wtforms import validators, ValidationError




class LoginForm(Form):
    id = StringField('UserName', [validators.DataRequired('Please enter your name.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    submit = SubmitField('Login')

class RegisterForm(Form):
    id = StringField('UserName', [validators.DataRequired('Please enter your name.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    submit = SubmitField('Register')



