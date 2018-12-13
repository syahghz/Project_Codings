from flask import *
from persistenceS import *
import uuid
import datetime

appS = Flask(__name__)

@appS.route("/")
def index():
    return render_template('NavBar.html')



@appS.route('/TrackProg', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        exer = request.form['exer']
        hours = request.form['hours']
        mins = request.form['mins']
        id = str(uuid.uuid4())
        date = datetime.date.today()
        error = None
        currentUsername = 'syahiirah' #'vera'
        storeBook(id, currentUsername, date, exer, hours, mins)

        tester = displaybook(id)
        request.form = ""

        return render_template('TrackProg.html', tester=tester)

    return render_template('TrackProg.html')



if __name__ == '__main__':
    appS.run()


