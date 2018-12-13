import shelve


book = shelve.open("book")
x = []
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

def displaybook(id):
    klist = list(book.keys())
    print(klist)
    x.clear()

    if id in klist:
        for i in klist:
            print('checkig...'+book[i].username)
            if book[i].username == 'syahiirah': #'vera'
                print(x)
                x.append(book[i])

        return x
    return ""

