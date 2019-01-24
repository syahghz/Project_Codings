from flask import *
from persistence import *


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)


@app.route('/init')
def init():
    init_db()
    return 'db initialised'






@app.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        elif not email:
            error = 'Email is required'
        else:
            user = get_user(username, password, email)
            if user is None:
                error = 'Wrong username and password and email'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                session['password'] = user.get_password()
                session['email'] = user.get_email()
                return'Success! Welcome! :)'
        flash(error)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        print('username: '+username+"!")
        password = request.form['password']
        print('password: ' + password + "!")

        #email = request.form['email']
        email = request.form.get('email', 'az@a.com')

        print('email: ' + email + "!")
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        elif not email:
            error ='Email is required'
        else:
            create_user(username, password, email)
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html')





@app.route('/logout')
def logout():
    session.clear()
    redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
