import shelve
import uuid
from datetime import date


class blog:
    def __init__(self, id):
        self.id = id
        self.dishName = ''
        self.ingredients = ''
        self.nutrition = ''
        self.instructions = ''
        self.file = ""
        self.created = ""
        self.username = ''
        # self.date = ""


datas = shelve.open("data")


def clear_data():
    klist = list(datas.keys())
    for key in klist:
        del datas[key]

#noted,LiQi:come back later add file
#def storeData(dishName, ingredients, nutrition, instructions, file):


def storeData(username, dishName, ingredients, nutrition, instructions, file):
    id = str(uuid.uuid4())
    data = blog(id)
    data.dishName = dishName
    data.ingredients = ingredients
    data.nutrition = nutrition
    data.instructions = instructions
    data.file = file
    data.username = username
    # data.created = str(date.today())
    data.created = str(date.today())
    datas[id] = data
    print(id)
    print("endhere")
def updateData(id,username, dishName, ingredients, nutrition, instructions, file):
    print(id)
    data= datas[id]


    data.dishName = dishName
    data.ingredients = ingredients
    data.nutrition = nutrition
    data.instructions = instructions
    data.file = file
    data.username = username
    data.created = str(date.today())
    datas[id] = data

def get_datas():
    klist = list(datas.keys())
    x = []
    for i in klist:
        x.insert(0, datas[i])

    return x


def update_data(data):
    print(datas)
    print(data.id)
    del datas[data.id]
    datas[data.id] = data
    print(datas)
    print("test2")


def delete_data(id):
    if id in datas:
        del datas[id]


def get_data(id):
    if id in datas:
        return datas[id]


def init_datas():
    clear_data()
    for i in range(5):
        storeData('user'+str(i), 'dishName'+str(i), 'ingredients'+str(i), 'nutrition'+str(i), 'instructions'+str(i), 'file')


