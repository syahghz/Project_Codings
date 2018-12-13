from flask import *
from persistenceThree import *





appThree = Flask(__name__)
appThree.config.from_mapping(
    SECRET_KEY='dev'
)


@appThree.route('/', methods=('GET', 'POST'))
def firstInput():

    if request.method == 'POST':
        w = request.form['weight']
        h = request.form['height']

        session["bmi"]=str(int(w)*(int(h)/int(h)))
        return redirect(url_for('nextplease'))

    return render_template('Input.html')

@appThree.route('/nextPlease', methods=('GET', 'POST'))
def nextplease():
    print('Next yesss')
    bmi=session["bmi"]
#    if request.method == 'POST':
 #       w = request.form['weight']
  #      h = request.form['height']
     #     cal = w/(h*h)
        #get the height
        #calculate the BMI, and store in variable
        #send the variable to this method below.

    return render_template('InputH.html',bmi =bmi)


# @appThree.route('/InputH')


if __name__ == '__main__':
    appThree.run()
