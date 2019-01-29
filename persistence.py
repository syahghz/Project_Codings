import shelve
import datetime
import uuid
import sqlite3
userinfo=shelve.open("userinfo")
IteminStore=shelve.open("IteminStore")
ACart=shelve.open("allcart")
users = shelve.open('user')
blogs = shelve.open('blog')
admins = shelve.open('admin')

import uuid
from datetime import date
# today = str(date.today())


class User:
    def __init__(self, id):
        self.__id = id
        self.__username = ''
        self.__password = ''
        self.__email=''

    def get_id(self):
        return self.__id

    def set_username(self, username):
        self.__username = username
    def set_password(self, password):
        self.__password = password
    def set_email(self,email):
        self.__email=email

    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    def get_email(self):
        return self.__email


def create_user(username, password,email):
    id = str(uuid.uuid4())
    user = User(id)
    user.set_username(username)
    user.set_password(password)
    user.set_email(email)
    users[id] = user

def get_user(username, password,email):
    klist = list(users.keys())
    for key in klist:
        user = users[key]
        print(user.get_username(), username, user.get_password(), password ,user.get_email(), email)
        if user.get_username() == username and user.get_password() == password and user.get_email()==email:
            return user
    return None

def update_user(id, user):
    users[id] = user
    return users[id]

def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]

def clear_blog():
    klist = list(blogs.keys())
    for key in klist:
        del blogs[key]

def add_user(user):
    users[user.get_id()] = user

def init_db():
    clear_user()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i),'email'+str(i) )















#my code

class Admin:
    def __init__(self, id):
        self.__id = id
        self.__username = ''
        self.__password = ''
        self.__email=''
        self.__pic=''
    def get_id(self):
        return self.__id
    def set_username(self, username):
        self.__username = username
    def set_password(self, password):
        self.__password = password
    def set_email(self,email):
        self.__email=email
    def set_pic(self,pic):
        self.__pic=pic
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    def get_email(self):
        return self.__email
    def get_pic(self):
        return self.__pic

def create_admin(username, password,email):
    id = str(uuid.uuid4())
    admin = Admin(id)
    admin.set_username(username)
    admin.set_password(password)
    admin.set_email(email)
    admins[id] = admin

def get_admin(username, password,email):
    klist = list(admins.keys())
    for key in klist:
        admin = admins[key]
        if admin.get_username() == username and admin.get_password() == password and admin.get_email()==email:
            return admin
    return None



class Item:
    def __init__(self,id):
        self.id=id
        self.pic=""
        self.type=""
        self.name=""
        self.price=""
        self.calories=""
        self.ingredient=""
        self.quantity=""
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_calories(self):
        return self.calories
    def get_ingredient(self):
        return self.ingredient


    def set_name(self,name):
        self.name=name
    def set_price(self,price):
        self.price=price
    def set_calories(self,calories):
        self.calories=calories
    def set_ingredient(self,ingredient):
        self.ingredient=ingredient



def Storing(pic,type,name,price,calories,ingredient,quantity):
    id = str(uuid.uuid4())
    ItemStore = Item(id)
    ItemStore.pic=pic
    ItemStore.type=type
    ItemStore.name = name
    ItemStore.price = price
    ItemStore.calories = calories
    ItemStore.ingredient = ingredient
    ItemStore.quantity = quantity
    ItemStore.created = str(date.today())
    IteminStore[id] = ItemStore

def update_iteminfo(info):
    IteminStore[info.id] = info


def get_itemallinfos():
    klist = list(IteminStore.keys())
    x = []
    for i in klist:
            x.append(IteminStore[i])
    return x



def get_itemallinfo(id):
    if id in IteminStore:
        return IteminStore[id]
    conn=IteminStore[id]
    cursor=conn.cursor()
    cursor.execute(IteminStore[id])
    melon_rows = cursor.fetchall()

    melons = []

    for row in melon_rows:
        melon = Item(row[0])

        melons.append(melon)

    return melons

allcart=[]
cart=[]
c=0
def Cart(item):

    id = str(uuid.uuid4())
    user = users(id)
    cart.append(item)

def submitcart():
    id = str(uuid.uuid4())
    user = users(id)
    user.created = str(date.today())
    users[id][cart] = cart
    allcart.append(cart)
    users[id][allcart]=allcart
    # clear_cart()

def get_cartallinfos():
    klist = list(users.keys())
    x = []
    for i in klist:
        x.append(users[i])
    return x

def get_cartallinfo(id):
    if id in users:
        return users[id]

def reducequantity(id,quantity):
    IteminStore[id].quantity-=quantity


def delete_itemadmin(id):
    if id in IteminStore:
        del IteminStore[id]

def delete_itemcart(id):

    if id in ACart:
        del ACart[id]


class editprofile(User):
    def __init__(self,id):
        super().__init__(id)
        self.__pic=""
        self.__goal=""
        self.__achievement=""

    def get_pic(self):
        return self.__pic
    def get_goal(self):
        return self.__goal
    def get_achievement(self):
        return self.__achievement

    def set_goal(self,goal):
        self.__goal=goal
    def set_achievement(self,achievement):
        self.__achievement=achievement
    def set_pic(self,pic):
        self.__pic=pic

class usergoal(User):
    def __init__(self,id,goal):
        super().__init__(id)
        self.__goal=goal
    def get_goal(self):
        return self.__goal


user=User(id)
def adduserinfo(id,goal,achievement,pic):
    # id = str(uuid.uuid4())

    info= editprofile(id)
    info.set_pic(pic)

    test1=goal
    while True:
        if test1.startswith(" "):
            test1= test1[1:]
        else:
            break
    info.set_goal(test1)

    test=achievement
    while True:
        if test.startswith(" "):
            test= test[1:]
        else:
            break

    info.set_achievement(test)
    for i in userinfo:
        if i==id:


            del userinfo[id]
            userinfo[id] = info

    userinfo[id] = info

    print(userinfo[id])
def userinfocallp(id):
    for i in userinfo:
        if i==id:
            bb=userinfo[i]
            # test1=bb.get_pic()

            # userinfo[i]=test1
            return bb.get_pic()
    return ""

def userinfocall(id):
    for i in userinfo:
        if i==id:
            aa=userinfo[i]
            print(aa.get_goal())
            # test1=aa.get_goal()
            # userinfo[id]=test1
            return aa.get_goal()
    return ""

def userinfocalle(id):
    for i in userinfo:
        if i==id:
            cc=userinfo[i]
            print(userinfo[i])
            print(cc.get_achievement())
            # test1=cc.get_achievement()
            return cc.get_achievement()

    return ""

def userinfocalldd(id):
    for i in userinfo:
        if i==id:
            dd=userinfo[i]
            return dd.get_birth()
    return ""

def update_userinfo(info):
    userinfo[info.id] = info

def get_allinfos():
    klist = list(userinfo.keys())
    x = []
    for i in klist:
        x.append(userinfo[i])
    return x

def get_allinfo(id):
    if id in userinfo:
        return userinfo[id]

def reduce():
    for i in ACart:

        itemCart=ACart[i]
        for u in IteminStore:

            if IteminStore[u].name ==ACart[i].name:
                item=IteminStore[u]
                if int(item.quantity)>=int(itemCart.quantity):
                    print(item.quantity)
                    item.quantity=int(item.quantity)-int(itemCart.quantity)
                    del IteminStore[u]
                    IteminStore[u]=item
    deleteCart()


def deleteCart():
    for i in ACart:
        del ACart[i]


def storeintocart(id,quantity):
    print(len(ACart))
    ACart[str(len(ACart))]=IteminStore[id]
    test1=ACart[str(len(ACart)-1)]
    test1.quantity=quantity
    test1.price=float(test1.price)*int(test1.quantity)
    test1.calories=int(test1.calories)*int(test1.quantity)
    del ACart[str(len(ACart)-1)]
    ACart[str(len(ACart)-1)]=test1

def give_ACartDict():
    return ACart

def give_ACart():
    klist = list(ACart.keys())
    x = []
    for i in klist:
        x.append(ACart[i])
    return x
