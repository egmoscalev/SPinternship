
"""
Дан список элементов произвольной природы. Необходимо разработать метод
max_odd(array), который определит максимальный нечетный элемент (21.000 = 21 и
тоже считается нечетным элементом). Вернуть None, если таких элементов нет в
переданном массиве.
"""

def max_odd(mylist):
  n = None
  for i in mylist:
    if isinstance(i,int) or (isinstance(i,float) and i % 1 == 0):
      if i % 2 != 0:
        if n == None or n < i:
          n = int(i)
  
  #print(n)
  return n

#test
max_odd([1, 2, 3, 4, 4])
# => 3
max_odd([21.0, 2, 3, 4, 4])
# => 21
max_odd(['ololo', 2, 3, 4, [1, 2], None]) # => 3
max_odd(['ololo', 'fufufu'])
# => None
max_odd([2, 2, 4])
# => None