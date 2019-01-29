from flask import *
from persistenceThree import *


from wtforms import Form



appThree = Flask(__name__)
appThree.config.from_mapping(
    SECRET_KEY='dev'
)


@appThree.route('/', methods=('GET', 'POST'))
def firstInput():

    if request.method == 'POST':
        w = float(request.form['weight'])
        h = float(request.form['height'])

        session["bmi"] = str(float(w) / (float(h) * float(h)) *float(703))


        ching = storingBMI(id, h, w, sum=getting_sum(w,h))




        return redirect(url_for('nextplease', ching=ching))

    return render_template('Input.html',)


@appThree.route('/nextPlease', methods=('GET', 'POST'))
def nextplease():
    print('Next yesss')

    bmiFloat = float(session["bmi"])
    resulttext = ''
    textFileToRead = ''
    name =''



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





    return render_template('InputH.html', resulttext=advice , bmiFloat=bmiFloat)

@appThree.route("/123123123")
def beginner():
    return render_template("Beginner.html")

@appThree.route('/BlackPanther')
def video():
    return render_template('Video.html')
@appThree.route('/WinterSoldier')
def bmiandbp():
    return render_template('BMI and BP.html')





@appThree.route('/heyo', methods=['GET','POST'])
def percentage():
    print('rt')


    if request.method == 'POST':
       age = request.form['age']
       weight = float(request.form['weight'])
       height = float(request.form['height'])
       bmi = float (request.form['bmi'])
       session['bmi']= str(float(weight) / (float(height) * float(height)) *float(703))
       session['pb'] = str(float(1.20) * float(bmi) + float(0.23)* int(age) - float(16.2))

       store=store_measurements(age, weight,height,bmi, total=session['pb'])


       return redirect(url_for('result',store=store))

    return render_template('Body_Percentage.html')





@appThree.route('/we', methods=('GET', 'POST'))
def result():

    maleFloat = float(session['pb'])
    enter = ''


    if 2<= maleFloat<= 4:
        enter = 'Essential Fat'

    elif 6<=maleFloat<=13:
        enter ='Athletes'

    elif 14 <= maleFloat <=17:
        enter = 'Fit'

    elif 18 <=maleFloat <= 25:
        enter ='Acceptable'

    elif maleFloat>25:
        enter = 'Obese'

    else:
        print('hi')

    return render_template('Bodyresult.html', enter=enter, maleFloat=maleFloat)

@appThree.route('/EXO', methods=('GET', 'POST'))
def laa():
    if request.method == 'POST':
        age = request.form['age']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = float(request.form['bmi'])
        session['bmi'] = str(float(weight) / (float(height) * float(height)))


        session['bp'] = str(float(1.20)* float(bmi) + (float(0.23) * int(age)) - float(5.4))

        psh=store_measurements(age,weight,height,bmi,total=session['bp'])

        return redirect(url_for('result2', psh=psh))

    return render_template('Body_Percentage2.html')

@appThree.route('/wewillrocku', methods=('GET', 'POST'))
def result2():

    femaleFloat = float(session['bp'])
    enter = ''
    result=''

    if 10<= femaleFloat<= 12:
        enter = 'Essential Fat'

    elif 13<=femaleFloat<=20:
        enter ='Athletes'

    elif 21 <= femaleFloat <=24:
        enter = 'Fit'

    elif 25 <=femaleFloat <= 31:
        enter ='Acceptable'

    elif femaleFloat>32:
        enter = 'Obese'

    else:
        print('hi')
        result= 'again'
    return render_template('Bodyresult2.html', enter=enter, result=result, femaleFloat=femaleFloat)

@appThree.route('/last')
def last():
    display = get_measurements()
    nodisplay = displayBMI()
    havedisplay =get_measurements()


    return render_template('history.html', display=display, help=nodisplay, fff=havedisplay)
if __name__ == '__main__':
    appThree.run(debug=True)
    appThree.run(port=80)
