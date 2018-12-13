
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



