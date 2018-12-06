from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('NavBar.html')

@app.route("/TrackProg")
def TrackProg():
    return render_template('TrackProg.html')

@app.route('/TrackProg', methods=('GET', 'POST'))
def register():
    return render_template('TrackProg.html')


if __name__ == '__main__':
    app.run()


