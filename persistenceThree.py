import shelve
import uuid
from datetime import date

#Body Percentage
class BodyPercentage:
    def __init__(self,id,total):
        self.__id=id
        self.__age = 0
        self.__weight = 0.0
        self.__height = 0.0
        self.__bmi = 0.0
        self.__gender =""
        self.__total =total


    def get_id(self):
        return self.__id
    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age

    def get_weight(self):
        return self.__weight
    def set_weight(self, weight):
        self.__weight = weight

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_bmi(self):
         return self.__bmi
    def set_bmi(self, bmi):
        self.__bmi=bmi

    def get_total(self):
         return self.__total
    def set_total(self, total):
        self.__total= total
    def set_gender(self,gender):
        self.__gender=gender










age = shelve.open('ages')
measurements = shelve.open('measure')
bmiAll = shelve.open('bmis')





def get_age(aging):
        if aging in age:
            ages = age[aging]
            if ages.aging == aging:
                return ages


def get_ages():
    age_list = []
    alist= list(age.keys())
    for key in alist:
        age_list.append(age[key])

    return age_list


def store_measurements(gender,age, weight, height, bmi, total):
    id = str(uuid.uuid4())
    measure = BodyPercentage(id,total)
    measure.set_age(age)
    measure.set_gender(gender)
    print(gender)
    print(measure.get_gender())
    print("thistime")
    measure.set_weight(weight)
    measure.set_height(height)
    measure.set_bmi(bmi)
    measure.set_total(total)
    print("test1")
    print(measure.get_total())
    print(total)
    print('this')
    measure.created = str(date.today())

    measurements[id] = measure

def calculations(bmi,age):
  total = float(1.20) * float(bmi) + float(0.23)* int(age) - float(16.2)
  print(total)
  return total

def get_measurements():
    print("gggggggggggggggggggggggggggggggggggggg")
    klist = list(measurements.keys())
    x = []
    for i in klist:
        x.append(measurements[i])
    print(x)
    print("here")
    return x



#BMI

class BMI:
    def __init__(self,id):
        self.__id=id
        self.__weight = 0.0
        self.__height = 0.0
        self.__sum =0.0

    def get_id(self):
        return self.__id

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_sum(self):
        return self.__sum

    def set_sum(self, sum):
        self.__sum = sum




def storingBMI(id,h, w, sum):
    id=str(uuid.uuid4())
    bmis= BMI(id)
    bmis.set_height(h)
    bmis.set_weight(w)
    bmis.set_sum(sum)
    bmis.created = str(date.today())
    bmiAll[id] = bmis

def getting_sum(w,h):
    totalbmi = float(w) / (float(h) * float(h)) *float(703)
    return totalbmi


def displayBMI():
    print("gggggggggggggggggggggggggggggggggggggg")
    klist = list(bmiAll.keys())
    x = []
    for i in klist:
        x.append(bmiAll[i])
    print(x)
    return x




















