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
        except:
            pass
        finally:
            return False
    
    def is_delicious(self):
        return True
    
