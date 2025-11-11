""""
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).
"""

class Dessert:

    def __init__(self,name = None ,calories = 0):
        self.set_name(name)
        self.set_calories(calories)
    
    def set_name(self,v):
        self.name = v
    
    def get_name(self):
      return self.name
    
    def set_calories(self, v):
        self.calories = v
    
    def get_calories(self):
      return self.calories
        

    def is_healthy(self):
        try:
            if (self.calories < 200):
                return True
            return False
        except:
            return False
    
    def is_delicious(self):
        return True
    
dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
#test_name
dessert.name = "test_name2"
print(dessert.name)
#test_name2
if dessert.name != "test_name2": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
print(dessert.calories)
#test_calories
dessert.calories = "test_calories2"
print(dessert.calories)
#test_calories2
if dessert.calories != "test_calories2": raise Exception("Setter for calories is not working")
print(dessert.is_delicious())
#True
if not dessert.is_delicious(): raise Exception("Invalid method result")
print(dessert.is_healthy())
#False
dessert.calories = 300
print(dessert.calories)
#300
print(dessert.is_healthy())
#False
if dessert.is_healthy(): raise Exception("Logical error. Method must return False")
print(dessert.is_delicious())
#True
if not dessert.is_delicious(): raise Exception("Invalid method result")
dessert.calories = 200
print(dessert.calories)
#200
print(dessert.is_healthy())
#False
if dessert.is_healthy(): raise Exception("Logical error. Method must return False")
dessert.calories = 199.99999
print(dessert.is_delicious())
#True
if not dessert.is_delicious(): raise Exception("Invalid method result")
print(dessert.calories)
#199.9999
print(dessert.is_healthy())
#False
if not dessert.is_healthy(): raise Exception("Logical error. Method must return True")