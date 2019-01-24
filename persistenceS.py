import shelve
import matplotlib.pyplot as plt
import random
import matplotlib
import os
import datetime
import calendar


book = shelve.open("book")
x = []


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



def storeBook(id, username, date, exercise, hour, mins):
    bok = AllBooks()
    bok.username = username
    bok.date = date
    bok.exercise = exercise
    bok.hour = hour
    bok.mins = mins

    exist = False

    book[id] = bok


def displaybook(currentUserLogin):
    #'Renjun': #'vera'
    currentUserLogin = 'Renjun'
    klist = list(book.keys())
    print(klist)
    x.clear()

    #if currentUserLogin in klist:
    for i in klist:
        print('checking...'+book[i].username)
        if book[i].username == currentUserLogin:
            print(x) #check if empty or not
            x.insert(0, book[i])
    return x


def graph(exer,hour,min):
    x_axis = []
    y_axis = []
    now = datetime.datetime.now()
    no_of_days=calendar.monthrange(now.year, now.month)[1]
    # x_axis = []
    print(now.year, now.month)
    for i in range(no_of_days + 1)[1::]:
        x_axis.append(i)
    print(x_axis)


# corresponding y axis values

    ex = exer
    hr = hour * 60
    min = min
    ttime = hr + min

    if ex == "Vigorous":
        val = 5
        m = float(val * ttime)
        if m > 100:
            s = m // 100
        elif m >= 10:
            s = m // 10
        elif m < 10:
            s = m

    elif ex == "Moderate":
        val = 3
        m = float(val * ttime)
        if m > 100:
            s = m // 100
        elif m >= 10:
            s = m // 10
        elif m < 10:
            s = m

    elif ex == 1:
        val = 1
        m = float(val * ttime)
        if m > 100:
            s = m // 100
        elif m >= 10:
            s = m // 10
        elif m < 10:
            s = m
    s += s
    y_axis.append(s)
    print(y_axis)



    # plotting the points
    da = matplotlib.dates.drange(x_axis[0], x_axis[-1], 1)
    plt.xlim(da)
    plt.ylim(y_axis[0], y_axis[-1])
    plt.plot(x_axis, y_axis)

    # naming the x axis
    plt.xlabel('Days in Month')
    # naming the y axis
    plt.ylabel('Progress')



    # giving a title to my graph
    plt.title('Progress by Day')

    # function to show the plot
    print('before')

    if len(os.listdir('C:\Y1 SEM 2\OOPP\SCodings\static\images')) != 0:
          for file in os.listdir('C:\Y1 SEM 2\OOPP\SCodings\static\images'):
                if "graph" in file:
                     print(file)
                     print('correct')
                     graphFile = open('graphFile.txt', 'r')
                     print("Directory is not empty")
                     print('gah1')
                     d = graphFile.read()
                     print(d)
                     s = d.partition('\static')
                     print(s)
                     os.remove('C:\Y1 SEM 2\OOPP\SCodings' + s[1] + s[2])
                     graphFile.close()

      # n = random.randint(0, 100)
      # print(n)

    # save new
    plt.savefig('C:\Y1 SEM 2\OOPP\SCodings\static\images\graph' + datetime.datetime.today().strftime('%Y-%m-%d') + '.png')
    print('boleh')

    # (in persistence?)
    # inheritence(onclick)
    # while True:
    #     if month == 1:
    #     if month ==2:

    # make new
    graphFile = open('graphFile.txt', 'w')
    graphFile.write('..\static\images\graph' + datetime.datetime.today().strftime('%Y-%m-%d') + '.png')
    # count += 1
    graphFile.close()
    print('stored')

        # return render_template('index.html')

# # class checkHour(AllBooks):
# #     def __init__(self, ):


# g = graph()

