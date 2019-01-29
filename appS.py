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
            rtime = dt.strftime("%I:%M:%S %p")
            print(rtime)
            error = None
            currentUsername = 'xuxi' #'vera'
            storeBook(id, currentUsername, date, rtime,  exer, hours, mins)

            tester = displaybook(currentUsername)
            user_reward = calc_reward(exer, hours, mins, currentUsername)
            if path.exists('point_File' + currentUsername + '.txt'):
                print('bacefile')
                point_File = open('point_File' + currentUsername + '.txt', 'r')
                prevpoints = point_File.read()
                num = float(prevpoints)
                point_File.close()
                points = int(num)
                return render_template('TrackProg.html', tester=tester, points=points)

            else:
                return render_template('TrackProg.html', tester=tester, points=0)


    else:
        currentUsername = 'xuxi'
        tester = displaybook(currentUsername)
        if path.exists('point_File' + currentUsername + '.txt'):
            point_File = open('point_File' + currentUsername + '.txt', 'r')
            prevpoints = point_File.read()
            num = float(prevpoints)
            point_File.close()
            points = int(num)
            print(points, 'in else')
            return render_template('TrackProg.html', tester=tester, points=points)
        else:
            points = 0
            print('tkde file utk bace')
            return render_template('TrackProg.html', tester=tester, points=points)

    return render_template('TrackProg.html', tester=tester)

@appS.route('/voucher')
def voucher():
    vlist = []
    currentUsername = 'xuxi'
    id = str(uuid.uuid4())
    dt = datetime.datetime.now()
    date = dt.strftime("%d") + " " + dt.strftime("%B") + " " + dt.strftime("%Y")


    if path.exists('point_File' + currentUsername + '.txt'):
        print('bacefile')
        point_File = open('point_File' + currentUsername + '.txt', 'r')
        prevpoints = point_File.read()
        num = float(prevpoints)
        point_File.close()
        points = float(num)
        if points >= 50:
                voucher_code = gen_num(id, date, currentUsername)
                print('moving on')
                print(voucher_code)
                k = list(voucher_code.keys())
                print(k)
                point_File = open('point_File' + currentUsername + '.txt', 'w')
                aftpoints = points - 50
                leftpoints = point_File.write("{}".format(aftpoints))
                print(leftpoints)
                point_File.close()
                print(aftpoints)

                return render_template('voucher.html', vlist=voucher_code, k=k)

        return render_template('voucher.html')


    return render_template('voucher.html')

@appS.route('/del')
def del_list():
    val = '1'
    k = list(voucher_code.keys())
    for i in k:
        print(i)
        voucher_code.pop(i)
        print('wee')
        return render_template('payment.html')
    # print(a)
    # del voucher_code[i]

    redirect(url_for('payment'))




#
# @appS.route('/TrackProg', methods=('GET', 'POST'))
# def add():
#     if request.method == 'POST':
#             exer = request.form['exer']
#             hours = request.form['hours']
#             mins = request.form['mins']
#             id = str(uuid.uuid4())
#             dt = datetime.datetime.now()
#             date = dt.strftime("%d") + " " + dt.strftime("%B") + " " + dt.strftime("%Y")
#             error = None
#             currentUsername = 'xuxi' #'vera'
#             storeBook(id, currentUsername, date, exer, hours, mins)
#
#             tester = displaybook(currentUsername)
#             user_reward = calc_reward(exer, hours, mins, currentUsername)
#             if path.exists('point_File' + currentUsername + '.txt'):
#                 print('bacefile')
#                 point_File = open('point_File' + currentUsername + '.txt', 'r')
#                 prevpoints = point_File.read()
#                 num = float(prevpoints)
#                 point_File.close()
#                 points = int(num)
#                 # if points >= 50:
#                 #     ncode = gen_num(date, currentUsername)
#                 #     print(ncode, "passed through PS")
#                 #
#                 #     if ncode[0] == currentUsername:
#                 #             print(ncode[0], 'usernow')
#                 #             Rcode = ncode[-2]
#                 #             print(Rcode, 'the code')
#
#                 #     point_File = open('point_File' + currentUsername + '.txt', 'w')
#                 #     aftpoints = points - 50
#                 #     leftpoints = point_File.write("{}".format(aftpoints))
#                 #     print(leftpoints)
#                 #     point_File.close()
#                 #     return render_template('TrackProg.html', tester=tester, points=points)
#                 # else:
#                 #     print('tkde')
#                 #     return render_template('TrackProg.html', tester=tester, points= 0)
#                 return render_template('TrackProg.html', tester=tester, points=points)
#             else:
#                 return render_template('TrackProg.html', tester=tester, points=0)
#
#
#     else:
#         currentUsername = 'xuxi'
#         tester = displaybook(currentUsername)
#         if path.exists('point_File' + currentUsername + '.txt'):
#             point_File = open('point_File' + currentUsername + '.txt', 'r')
#             prevpoints = point_File.read()
#             num = float(prevpoints)
#             point_File.close()
#             points = float(num)
#             print(points, 'in else')
#             return render_template('TrackProg.html', tester=tester, points=points)
#         else:
#             points = 0
#             print('tkde file utk bace')
#             return render_template('TrackProg.html', tester=tester, points=points)
#
#
#     return render_template('TrackProg.html', tester=tester)


if __name__ == '__main__':
    appS.run()


