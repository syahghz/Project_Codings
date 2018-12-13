import shelve
userinfo=shelve.open("userinfo")

class Item:
    def __init__(self,name,price,calories):
        self.name=name
        self.price=price
        self.calories=calories
    # def get_name(self):
    #     return self.__name
    # def get_price(self):
    #     return self.__price
    # def get_calories(self):
    #     return self.__calories
    #
    # def set_name(self,name):
    #     self.__name=name
    # def set_price(self,price):
    #     self.__price=price
    # def set_calories(self,calories):
    #     self.__calories=calories

class Food(Item):
    def __init__(self,name,price,calories,ingredient):
        super().__init__(name,price,calories)
        self.ingredient=ingredient

    # def get_ingredient(self):
    #     return self.__ingredient


class drink(Item):
    def __init__(self,name,price,calories):
        super().__init__(name,price,calories)


class Store:
    fooddetail={"Soba noodle":{"name":"Soba noodle","price":"$3.50","calories":"205","ingredient":"green soybeans,low sodium soy sauce,fresh lime juice,sesame oil,cilantro,green onion,Sesame seeds,For a spicy alternative,weet chili sauce or sriracha sauce","pic":"soba_noodles.jpg"},
                "thai noodle salad":{"name":"thai noodle salad","price":"$4","calories":"235","ingredient":"bean sprout,limes,zests and juice,salt-reduced soy sauce,brown sugar,red onion,carrot,spring onion,red capsicums,tomatoes,cucumber,lettuces,pork mince,ginger,garlic,chili powder"}
                ,"Roasted Cauliflower and Broccoli":{"name":"Roasted Cauliflower and Broccoli","price":"$4.50","calories":"320","ingredient":"cauliflower,broccoli,garlic,olive oil,teaspoon salt"}
                }
    foodname=["Soba noodle","thai noodle salad","Roasted Cauliflower and Broccoli"]
    # def Storing(self):
    #     f1=Food("Soba noodle","$3.50","205","green soybeans,low sodium soy sauce,fresh lime juice,sesame oil,cilantro,green onion,Sesame seeds,For a spicy alternative,weet chili sauce or sriracha sauce")
    #     Store.fooddetail[f1.name]=f1
    #     f2=Food("thai noodle salad","$4","235","bean sprout,limes,zests and juice,salt-reduced soy sauce,brown sugar,red onion,carrot,spring onion,red capsicums,tomatoes,cucumber,lettuces,pork mince,ginger,garlic,chili powder")
    #     Store.fooddetail[f2.name]=f2
    #     f3=Food("Roasted Cauliflower and Broccoli","$4,50","320","cauliflower,broccoli,garlic,olive oil,teaspoon salt")
    #     Store.fooddetail[f3.name]=f3

    cart={}
    def Cart(self,item):

        Store.cart[item.name]=item
    #def add_items(self,item):
     #   Cart.cart[item.get_name]=item
# def display():
#     klist = list(Store.fooddetail.keys())
#     x = []
#     for i in klist:
#         x.append(Store.fooddetail[i])
#     return x
# s=Store()
# s.Storing()























#Nicole's code
import shelve
import uuid
from datetime import date
# today = str(date.today())

class User:
    def __init__(self, id):
        self.__id = id
        self.__username = ''
        self.__password = ''

    def get_id(self):
        return self.__id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

class Blog:
    def __init__(self, id):
        self.id = id
        self.username = ''
        self.title = ''
        self.body = ''
        self.created = ''

users = shelve.open('user')
blogs = shelve.open('blog')

def create_blog(username, title, body):
    id = str(uuid.uuid4())
    blog = Blog(id)
    blog.title = title
    blog.username = username
    blog.body = body
    blog.created = str(date.today())
    blogs[id] = blog

def update_blog(blog):
    blogs[blog.id] = blog

def delete_blog(id):
    if id in blogs:
        del blogs[id]

def get_blogs():
    klist = list(blogs.keys())
    x = []
    for i in klist:
        x.append(blogs[i])
    return x

def get_blog(id):
    if id in blogs:
        return blogs[id]

def create_user(username, password):
    id = str(uuid.uuid4())
    user = User(id)
    user.set_username(username)
    user.set_password(password)
    users[id] = user

def get_user(username, password):
    klist = list(users.keys())
    for key in klist:
        user = users[key]
        print(user.get_username(), username, user.get_password(), password)
        if user.get_username() == username and user.get_password() == password:
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
    clear_blog()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i))
        create_blog('user'+str(i), 'title'+str(i), 'body'+str(i))






#my code

class editprofile(User):
    def __init__(self,id):
        super().__init__(id)
        self.__gender=""
        self.__goal=""
        self.__achievement=""
        self.__address=""
    def get_gender(self):
        return self.__gender
    def get_goal(self):
        return self.__goal
    def get_achievement(self):
        return self.__achievement
    def get_address(self):
        return self.__address

    def set_gender(self,gender):
        self.__gender=gender
    def set_goal(self,goal):
        self.__goal=goal
    def set_achievement(self,achievement):
        self.__achievement=achievement
    def set_address(self,address):
        self.__address=address

