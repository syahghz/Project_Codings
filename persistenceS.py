import shelve
# import matplotlib.pyplot as plt
import random
# import matplotlib
import os.path
from os import path
from datetime import datetime
from datetime import timedelta
# import calendar


book = shelve.open("book")
x = []
voucher_list =[]


# def is_empty(list):
#     if list:
#         print('Structure is not empty.')
#         return False
#     else:
#         print('Structure is empty.')
#         return True
class AllBooks:
    def __init__(self):
        self.exercise = ''
        self.hour = 0
        self.mins = 0
        self.date = ""
        self.username = ""
        print(self.hour)
        print('the class')




def storeBook(id, username, date, exercise, hour, mins):
    bok = AllBooks()
    bok.username = username
    bok.date = date
    bok.exercise = exercise
    bok.hour = hour
    bok.mins = mins

    exist = False

    book[id] = bok
    print(book[id])
    print('masuk storebook')
    return bok.exercise


def displaybook(currentUserLogin):
    #'Renjun': #'vera'
    # currentUserLogin = 'Renjun'
    klist = list(book.keys())
    print(klist)
    x.clear()

    #if currentUserLogin in klist:
    for i in klist:
        # print('checking...'+book[i].username)
        if book[i].username == currentUserLogin:
            print('displaybook', currentUserLogin)
            print('showdbook', book[i].username)
            # print(x) #check if empty or not
            x.insert(0, book[i])
    print('masuk display')
    return x

def calc_reward(exercise, hour, mins, currentUserLogin):
    print(currentUserLogin)
    print('going in')
    reward = AllBooks
    # ex = AllBooks(exercise)
    reward.exercise = exercise #betul
    print(reward.exercise)
    reward.hour = float(hour) * 60 #BETUL
    print(reward.hour)
    reward.mins = float(mins) #BETUL
    print(reward.mins)
    ttime = float(reward.hour + reward.mins) #BETUL
    print(ttime)
    print('calculating now')

    if reward.exercise == "Vigorous":
        val = 5
        print(val)
        m = float(int(val) * int(ttime))
        print(m, "V")
        if m > 100:
            s = m // 100
        elif m >= 10:
            s = m // 10
        elif m < 10:
            s = m

    elif reward.exercise == "Moderate":
        val = 3
        m = float(val * ttime)
        print(m, "M")
        if m > 100:
            s = m // 100
            print('divide 100', s)
        elif m >= 10:
            s = m // 10
            print('divide 10', s)
        elif m < 10:
            s = m
            print('tk divide', s)

    elif reward.exercise == "Light":
        val = 1
        m = float(val * ttime)
        print(m, "L")
        if m > 100:
            s = m // 100
        elif m >= 10:
            s = m // 10
        elif m < 10:
            s = m
    print(s, 'before')
    # s += s
    # print(s, "ape ni")

    print('loop!')
    # pstore = list(book.keys())
    # for i in pstore:
    #     print(i)
    #     print(book[i].username, 'the book i')
    #     for u in book[i].username:
    #         if book[i].username == currentUserLogin:
    keys = list(book.keys())
    for ind in keys:
        print(ind)
        # print(book[i].username)
        # for u in book[ind].username:
        #     print('masuk u')
        #     print(u)
        #     print(currentUserLogin)
        if book[ind].username == currentUserLogin:
                print(book[ind].username)
                print(currentUserLogin)
                if path.exists('point_File' + book[ind].username + '.txt'):
                    print('file ade')
                    print('alright to reading in file!!')
                    point_File = open('point_File' + book[ind].username + '.txt', 'r')
                    prevpoints = point_File.read()
                    num = float(prevpoints)
                    point_File.close()
                    print(prevpoints, 'dh baca')

                    point_File = open('point_File' + book[ind].username + '.txt', 'w')
                    newpoints = (num + int(s))
                    print(newpoints)
                    npoints = point_File.write( "{}\n".format(newpoints))
                    point_File.close()
                    print(npoints, 'dh tukar')

                    break

                else:
                    print('file tkde')
                    print(s)
                    point_File = open('point_File' + book[ind].username + '.txt', 'w')
                    firstpoints = point_File.write( "{}".format(s))
                    print(firstpoints)
                    point_File.close()

                    print('jadi tk')
                    break
        else:
            print('masuk else')
            continue

    # continue
    print('out')


def gen_num(date, currentUsername):
    currentUserList = []
    #generate the code number
    num = random.randint(1000,10000)
    print(num)
    Dcode = "WW" + str(num)
    print(Dcode)

    #take the expiry date
    datexp = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
    print(datexp)

    currentUserList.append(currentUsername)
    currentUserList.append(date)
    currentUserList.append(Dcode)
    currentUserList.append(datexp)
    print(currentUserList)
    return currentUserList
