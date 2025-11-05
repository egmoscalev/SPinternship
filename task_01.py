"""
Разработайте метод is_palindrome(string), который будет определять, является ли
параметр string палиндромом (строкой, которая читается одинаково как сначала
так и с конца), при условии игнорирования пробелов, знаков препинания и
регистра.
Тесты для примеров и проверки:
is_palindrome("A man, a plan, a canal -- Panama")
is_palindrome("Madam, I'm Adam!")
is_palindrome(333)
is_palindrome(None)
is_palindrome("Abracadabra")
# => True
# => True
# => True
# => False
# => False
# """

def is_palindrome (s = None):
  string = str(s)
  string = string.casefold()
  out = ''
  
  for i in range(len(string)):
    n = ord(string[i])
    if (n >= 48 and n <= 57 or n >= 97 and n <= 122):
      out += (string[i])
  
  if (out == out[::-1]):
    #print(True)
    return True
  else:
    #print(False)
    return False

#test
is_palindrome("A man, a plan, a canal -- Panama")
is_palindrome("Madam, I'm Adam!")
is_palindrome(333)
is_palindrome(None)
is_palindrome("Abracadabra")