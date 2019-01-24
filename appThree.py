from flask import *

import math

from wtforms import Form



appThree = Flask(__name__)
appThree.config.from_mapping(
    SECRET_KEY='dev'
)


@appThree.route('/', methods=('GET', 'POST'))
def firstInput():

    if request.method == 'POST':
        w = request.form['weight']
        h = request.form['height']

        session["bmi"] = str(float(w)/(float(h)*float(h)))





        return redirect(url_for('nextplease'))

    return render_template('Input.html',)


@appThree.route('/nextPlease', methods=('GET', 'POST'))
def nextplease():
    print('Next yesss')

    bmiFloat = float(session["bmi"])
    resulttext = ''
    textFileToRead = ''




    if bmiFloat <= 18.5:

        textFileToRead = "advice_underweight"

    elif 18.5 <= bmiFloat <= 24.9:

        textFileToRead = "advice_normalweight"

    elif 25<= bmiFloat <= 29.9:

        textFileToRead = 'advice_overweight.txt'

    elif bmiFloat >= 30:

        textFileToRead = 'advice_obese'

    else:
        print('Try again')


    advice_file = open(textFileToRead, 'r')
    #codes to read each line

    # line = advice_file.readline()
    #
    # while line:
    #     line=advice_file.readline()

    # line = "TESTTTTTTT"

    '''advicelst = []
    while True:
        # read line
        line = advice_file.readline()
        # in python 2, print line
        # in python 3
        print(line)
        advicelst.append(line)
        # check if line is not empty
        if not line:
            break
    advice_file.close()'''

    advice = []
    advice_file = open(textFileToRead, 'r')
    for line in advice_file:
        # in python 2
        # print line
        # in python 3

        advice.append(line)
    advice_file.close()





    return render_template('InputH.html', resulttext=advice , bmiFloat=bmiFloat )

@appThree.route("/123123123")
def beginner():
    return render_template("Beginner.html")

@appThree.route('/BlackPanther')
def video():
    return render_template('Video.html')

@appThree.route('/heyo', methods=['GET','POST'])
def percentage():

    if request.method['POST']:
       weight = request.form['weight']
       height = request.form['height']
       wa = request.form['waist']
       neck = request.form['neck']
       hip = request.form ['hip']



       session['bp'] =float(495/(1.29579-(0.35004*math.log10(wa+hip-neck))+(0.22100*math.log10(height))) - 450)

       return redirect(url_for('letmego'))

    return render_template('Body Percentage.html')


@appThree.route('/EXO')
def letmego():
    print('fighting')
    body = session['bp']


    return render_template('Bodyresult.html', body=body)





if __name__ == '__main__':
    appThree.run(debug=True)
    appThree.run(port=80)
