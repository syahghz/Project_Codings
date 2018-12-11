from flask import Flask, render_template
from flask import request
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
    TraTab = []
    if request.method == 'POST':
        exer = request.form['exer']
        hours = request.form['hours']
        mins = request.form['mins']
        error = None

        TraTab[datetime.date] = exer, hours, mins
    return render_template('TrackProg.html')



if __name__ == '__main__':
    app.run()


