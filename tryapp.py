from flask import *
from app import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ebaec4092587f550f6790781ba2271b4'

@app.route("/")
@app.route("/home")
def home():
    return render_template('test.html')

@app.route("/about")
def about():
    return render_template('answers.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('Bodyresult.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()

    return render_template('lol.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)




