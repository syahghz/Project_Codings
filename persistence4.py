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
        
datas = shelve.open("data")

def clear_data():
    klist = list(datas.keys())
    for key in klist:
        del batas[key]

#noted,LiQi:come back later add file
#def storeData(dishName, ingredients, nutrition, instructions, file):
def storeData(dishName, ingredients, nutrition, instructions, file):
    id = str(uuid.uuid4())
    data = blog(id)
    data.dishName = dishName
    data.ingredients = ingredients
    data.nutrition = nutrition
    data.instructions = instructions
    data.file = file
    data.created = str(date.today())
    datas[id] = data

def init_datas():
    clear_data()
    for i in range(5):
        storeData('user'+str(i), 'dishName'+str(i), 'ingredients'+str(i), 'nutrition'+str(i), 'instructions'+str(i), 'file')


def get_datas():
    klist = list(datas.keys())
    x = []
    for i in klist:
        x.append(datas[i])

    return x

# def get_latestrecipe():
#     klist = list(datas.keys())
#     x = []
#     if klist:
#         print('what is here???'+klist[-1])
#         x.append(klist[-1])
#
#     return x

# def update_data(data):
#     datas[data.id] = data
#
# def delete_data(id):
#     if id in datas:
#         del datas[id]
# 
# def get_data(id):
#     if id in datas:
#         return datas[id]
# 
# def add_user(user):
#     users[user.get_id()] = user
# 
# def init_db():
#     clear_user()
#     clear_data()
#     for i in range(5):
#         create_user('user'+str(i), 'pass'+str(i))
#         storeData('user'+str(i), 'title'+str(i), 'body'+str(i))
