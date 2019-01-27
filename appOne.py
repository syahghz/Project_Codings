from flask import *
from user import *
from tryapp import *
import functools

app = Flask(__name__, template_folder='templates')
app.config.from_mapping(
    SECRET_KEY='dev'
)

@app.route('/init')
def init():
    init_users()

    return 'db initialised'

@app.route('/')
def index():
    form = LoginForm(request.form)
    if 'username' in session:

        return render_template('lol.html' )
    else:
        return render_template('login.html', form = form)


@app.route('/login',  methods=('GET', 'POST'))
def login():
    login_form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        user = get_user(login_form.id.data, login_form.password.data)
        if user is None:
            error = 'Wrong username and password'
        else:
            session['username'] = user.username
            return redirect(url_for('index'))
        flash(error)
    return render_template('login.html', form=login_form)

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = form.id.data
        password = form.password.data
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            create_user(username, password)
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html', form=form)



@app.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=80)




