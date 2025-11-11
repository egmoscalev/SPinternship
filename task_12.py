""""
Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
геттером и сеттером для атрибута flavor (все параметры являются не
обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
false только в тех случаях, когда flavor равняется «black licorice».
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
    

class JellyBean(Dessert):
    def __init__(self,name = None,calories = 0, flavor = None):
        super().__init__(name,calories)
        self.set_flavor(flavor)

    def set_flavor(self,v):
        self.flavor = v

    def get_flavor(self):
        return self.flavor
    
    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        
        return True