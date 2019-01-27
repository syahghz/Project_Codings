from flask import *
from persistenceS import *
import uuid
import datetime
# import matplotlib.pyplot as plt
# import random
# import os

appS = Flask(__name__)

tester = 0

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
            dt = datetime.datetime.now()
            date = dt.strftime("%d") + " " + dt.strftime("%B") + " " + dt.strftime("%Y")
            # real_time =
            error = None
            currentUsername = 'mark' #'vera'
            storeBook(id, currentUsername, date, exer, hours, mins)

            tester = displaybook(currentUsername)
            request.form = ""
            # print(exer)
            user_reward = calc_reward(exer, hours, mins, currentUsername)
            if path.exists('point_File' + currentUsername + '.txt'):
                point_File = open('point_File' + currentUsername + '.txt', 'r')
                prevpoints = point_File.read()
                num = int(prevpoints)
                point_File.close()
                points = int(num)
                if points >= 50:
                    ncode = gen_num()
                    print(ncode, "passed through PS")
                    Dcode = "WW" + str(ncode)
                    print(Dcode)
                    point_File = open('point_File' + currentUsername + '.txt', 'w')
                    aftpoints = points - 50
                    leftpoints = point_File.write("{}\n".format(aftpoints))
                    print(leftpoints)
                    point_File.close()
                    return render_template('TrackProg.html', tester=tester, points=points, Dcode=Dcode)
                print('tkde')

                return render_template('TrackProg.html', tester=tester, points=points)

    else:
        currentUsername = 'mark'
        tester = displaybook(currentUsername)
        if path.exists('point_File' + currentUsername + '.txt'):
            point_File = open('point_File' + currentUsername + '.txt', 'r')
            prevpoints = point_File.read()
            num = int(prevpoints)
            point_File.close()
            points = int(num)

            return render_template('TrackProg.html', tester=tester, points=points)
        else:
            points = 0
            return render_template('TrackProg.html', tester=tester, points=points)


    return render_template('TrackProg.html', tester=tester)



if __name__ == '__main__':
    appS.run()


