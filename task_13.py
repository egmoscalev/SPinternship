"""
Напишите декоратор @cached, который кэширует результаты функции, чтобы
избежать повторных вычислений для одних и тех же аргументов. Декоратор
должен поддерживать:
• ограничение размера кэша: при превышении максимально хранимого
количества записей (max_size) удаляются самые старые записи:
• если max_size=None, то размер кэша не ограничен
• если max_size не соответствует целому числу, то также
инициализировать его как None
• время жизни записей: автоматически удалять результаты, сохранённые
более seconds назад:
• если seconds=None, то записи не устаревают
• размер кэша не ограничен, если seconds не соответствует целому
числу, то также инициализировать его как None
• декоратор должен учитывать как позиционные (*args), так и
именованные аргументы (**kwargs)
13Тесты для примеров и проверки:
@cached(max_size=3, seconds=10)
def slow_function(x):
print(f"Вычисляю для {x}...")
return x ** 2
# Первый вызов — вычисляется
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
# Повторный вызов с теми же аргументами — берётся из кэша
print(slow_function(2)) # Вывод: 4 (без вычисления)
# Через 15 секунд кэш устареет, и будет новое вычисление
time.sleep(15)
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
"""
from collections import deque
import time

class cachedCache:
    
    def __init__(self, max_size = None, seconds = None):

        if not isinstance(max_size,int) or max_size < 1:
            self.max_size = None
        else:
            self.max_size = max_size

        if not isinstance(seconds,int or float) or seconds <= 0:
            self.seconds = None
        else:
            self.seconds = seconds

        self.deque = deque()
        self.dictionary = dict() 

    def get(self, key):
        self.pop_old()
        if key in self.dictionary.keys():
            return self.dictionary[key]
        
        else:
            return None

    def add(self,key, results): # key это аргументы хешируемой функции
        
        self.pop_old()
        #если deque переполнена
        if len(self.deque) == self.max_size:
            self.pop()

        self.dictionary.setdefault(key,results) 
        self.deque.appendleft((key,time.time()))

    def pop(self):
        x = self.deque.pop() #key and time tuple
        del self.dictionary[x[0]]        

    def pop_old(self): 

        if self.seconds == None:
            return
        
        while len(self.deque) > 0:
            deltatime = time.time() - self.deque[-1][1]
            if deltatime > self.seconds:
                self.pop()
            else:
                break

            




def cached(max_size = None, seconds = None):

    def wrapper1(func):

        cache = cachedCache(max_size,seconds)

        def wrapper(*args, **kwargs):   
            key = (args, frozenset(kwargs.items())) #frozenset нужен чтобы сделать kwargs cacheble
            result = cache.get(key)

            if result != None:
                return result

            result = func(*args, **kwargs)
            cache.add(key,result) 
            return result
        
        return wrapper
    
    return wrapper1

#test

@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2
# Первый вызов — вычисляется
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
# Повторный вызов с теми же аргументами — берётся из кэша
print(slow_function(2)) # Вывод: 4 (без вычисления)
# Через 15 секунд кэш устареет, и будет новое вычисление
time.sleep(15)
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4

    
