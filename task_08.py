"""Написать метод multiply_numbers(inputs), который вернет произведение цифр,
входящих в inputs."""


def multiply_numbers(inputs = None):
  
  result = None
  
  if inputs is None:
    print (None)
    
  else:
    mylist = list(str(inputs))
  
    for i in mylist:
      n = ord(i)
      if n >= 48 and n <= 57:
        if result == None:
          result = 1
        result *= int(i)
  
    print (result)
    return (result)
      

#test

multiply_numbers()
# => None
multiply_numbers('ss')
# => None
multiply_numbers('1234')
# => 24
multiply_numbers('sssdd34') # => 12
multiply_numbers(2.3)
# => 6
multiply_numbers([5, 6, 4]) # => 120
