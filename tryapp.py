from flask import *
from persistenceOne import*
import functools

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['id'] is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view
@app.route('/init')
def init():
    init_db()
    return 'db initialised'

@app.route('/')
def index():
    if 'id' in session:

        return render_template('profile.html')
    else:
        return render_template('login.html')

@app.route('/login',  methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email=request.form['email']
        type=request.form.get('type')
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            if type=="User":
                user = get_user(username,password,email)
                if user is None:
                    error = 'Wrong username,password and email.'
                else:
                    session['id'] = user.get_id()
                    session['user_name'] = user.get_username()
                    session['email']=user.get_email()
                    return redirect(url_for('profile',id=session["id"]))
            elif type=="Admin":

                admin=get_admin(username,password,email)
                if admin is None:
                    error='Wrong username,password and email.'
                else:
                    session['id'] = admin.get_id()
                    session['user_name'] = admin.get_username()
                    session['email']=admin.get_email()
                    return redirect(url_for('adminaboutitem'))
        flash(error)
    return render_template('login.html', data=[{'type':'User'}, {'type':'Admin'}] )
@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email= request.form['email']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required'
        else:
            create_user(username, password, email)
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=80)
