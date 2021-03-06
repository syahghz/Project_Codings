import shelve
import uuid
import datetime
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


users =shelve.open('user')

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



def add_user(user):
    users[user.get_id()] = user

def init_db():
    clear_user()

    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i),'email'+str(i) )




