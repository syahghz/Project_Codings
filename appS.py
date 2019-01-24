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

@appS.route('/ProgUp')
def update():
    return render_template('ProgUP.html')


@appS.route('/TrackProg', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        # less = checkHour()
        #
        # if less <= 12:

            exer = request.form['exer']
            hours = request.form['hours']
            mins = request.form['mins']
            id = str(uuid.uuid4())
            dt = datetime.datetime.now()
            date = dt.strftime("%d") + " " + dt.strftime("%B") + " " + dt.strftime("%Y")
            error = None
            currentUsername = 'Renjun' #'vera'
            storeBook(id, currentUsername, date, exer, hours, mins)

            tester = displaybook(id)
            request.form = ""
            # print(exer)
            points = 50
            print("checking boleh ke tk ", tester)

            # print('jln sini ke tk')
            # graph(exer,hours,mins)
    #             #
    #             #
    #             # # read new
    #             # graphFile = open('graphFile.txt', 'r')
    #             # print('gah')
    #             # contents = graphFile.read()
    #             # print(contents)
    #             # graphFile.close()
    #             # print(contents)
    #             # return render_template('TrackProg.html', contents=contents, tester=tester)
            return render_template('TrackProg.html', tester=tester, points=points)
        # else:
        #     return less
    else:
        tester = displaybook('Renjun')
        points = 30
        return render_template('TrackProg.html', tester=tester, points=points)


# graph

    # print('jln sini ke tk')
    # callX = Xgraph()
    # callY = Ygraph()
    # plot(callX,callY)
    #
    #
    # # read new
    # graphFile = open('graphFile.txt', 'r')
    # print('gah')
    # contents = graphFile.read()
    # print(contents)
    # graphFile.close()
    # print(contents)
    # return render_template('TrackProg.html', contents =contents)
    return render_template('TrackProg.html', tester=tester)




if __name__ == '__main__':
    appS.run()


