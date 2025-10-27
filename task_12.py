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
        if not isinstance(v, str):
            if v != None:
                print("Name should be a string. Name set to None")
            self._name = None
        else:
            self._name = v
    
    def get_name(self):
      return self._name
    
    def set_calories(self, v):
        if not isinstance(v, int or float) or v < 0:
            if v != None:
                print("Calories should be a non-negative number. Calories set to 0")
            self._calories = 0
        else:
            self._calories = v
    
    def get_calories(self):
      return self._calories
        

    def is_healthy(self):
        if (self._calories < 200):
            return True
        
        return False
    
    def is_delicious(self):
        return True
    

class JellyBean(Dessert):
    def __init__(self,name = None,calories = 0, flavor = None):
        super().__init__(name,calories)
        self.set_flavor(flavor)

    def set_flavor(self,v):
        if not isinstance(v, str):
            if v != None:
                print("Flavor should be a string. Flavor set to None")
            self._flavor = None
        else:
            self._flavor = v

    def get_flavor(self):
        return self._flavor
    
    def is_delicious(self):
        if self._flavor == 'black licorice':
            return False
        
        return True
    