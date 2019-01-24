from wtforms import Form, BooleanField, StringField, DateTimeField, SubmitField,PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired
class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password =PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    birthday = DateTimeField('Birthday', format='%m/%d/%y', validators=[DataRequired()])
    accept_rules = BooleanField('I accept the site rules',validators=[InputRequired()])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    login = SubmitField('Login')








