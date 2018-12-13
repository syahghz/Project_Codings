import shelve

data = shelve.open("data")

class allData:
    def __init__(self):
        self.dishName = ''
        self.ingredients = ''
        self.nutrition = ''
        self.directions = ''

def storeData(dishName, ingredients, nutrition, directions):
    data = allData()
    data.dishName = dishName
    data.ingredients = ingredients
    data.nutrition = nutrition
    data.directions = directions
