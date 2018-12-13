from flask import *
from persistenceS import *
import uuid
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('NavBar.html')

'''@app.route("/TrackProg")
def TrackProg():
    return render_template('TrackProg.html')'''

@app.route('/TrackProg', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        exer = request.form['exer']
        hours = request.form['hours']
        mins = request.form['mins']
        id = str(uuid.uuid4())
        date = datetime.date.today()
        error = None
        currentUsername = 'vera' #''syahiirah'
        storeBook(id, currentUsername, date, exer, hours, mins)

        tester = displaybook(id)
        request.form = ""

        return render_template('TrackProg.html', tester=tester)

    return render_template('TrackProg.html')

@app.route('/Reward')
def calcr():
    print("rEwaRD")





if __name__ == '__main__':
    app.run()


