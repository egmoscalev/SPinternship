"""
Реализуйте класс EvenNumbers, который в конструкторе принимает целое число n
— количество чётных чисел для генерации. Итератор должен выдавать числа по
порядку, начиная с 0: 0, 2, 4, ..., 2*(n-1).
Тесты для примеров и проверки:
evens = EvenNumbers(5)
for num in evens:
print(num) # Должно вывести 0, 2, 4, 6, 8
"""

class EvenNumbers:

    def __init__(self, n = 0):
        if isinstance(n, int) and n >= 0:
            self.n = n
        else:
            self.n = 0
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            result = 2*self.current
            self.current += 1
            return result
        else:
            raise StopIteration
        

#test

evens = EvenNumbers(5)
for num in evens:
    print(num)