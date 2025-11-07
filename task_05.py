"""
Разработать метод date_in_future(integer), который вернет дату через integer дней.
Если integer не является целым числом, то метод должен вывести текущую дату.
Формат возвращаемой методом даты должен иметь следующий вид '24-03-2001
22:33:44'
"""


import datetime

def date_in_future(integer):
  if not isinstance(integer,int):
    date = datetime.datetime.now()

  else:
    date = datetime.datetime.now() + datetime.timedelta(days=integer)

  #print(date.strftime("%Y-%m-%d %H:%M:%S"))
  return date.strftime("%Y-%m-%d %H:%M:%S")

a = date_in_future([]) # => текущая дата
b = date_in_future(2) # => текущая дата + 2 дня

print(type(b),b)
