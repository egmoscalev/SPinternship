""""
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).
"""

class Dessert:

    def __init__(self,name = 'noname',calories = 1):
        self.set_name(name)
        self.set_calories(calories)
    
    def set_name(self,v):
        if not isinstance(v, str):
            print("Name should be a string. Name set to 'noname'")
            self._name = 'noname'
        else:
            self._name = v
    
    def get_name(self):
      return self._name
    
    def set_calories(self, v):
        if not isinstance(v, int or float) or v <= 0:
            print("Calories should be a positive number. Calories set to 1")
            self._calories = 1
        else:
            self._calories = v
    
    def get_calories(self):
      return self._calories
        

    def is_healthy(self):
        if (self._calories < 200):
            return True
        else:
            return False
    
    def is_delicious(self):
        return True
    
