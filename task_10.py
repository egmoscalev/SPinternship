"""

Разработайте функцию count_words(string), которая будет возвращать словарь со
статистикой частоты употребления входящих в неё слов. (числа считаются словами?)
Тесты для примеров и проверки:
count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,
"canal": 1, "panama": 1, "plan": 1}
count_words("Doo bee doo bee doo")
# => {"doo": 3, "bee": 2}

"""

def count_words(string = None):
  if (string == None or not isinstance(string,str)):
    return None
  string = string.casefold() + ' '
  words_list = []
  word = ''

  for i in range(len(string)):
    n = ord(string[i])
    if (n >= 97 and n <= 122):
      word += string[i]
    elif (word != '') :
      words_list.append(word)
      word = ''
  
  result = {}
    
  for i in words_list:
    key = ''.join(i)
    result.setdefault(key, 0)
    result[key] += 1
      
  return result;

#test

print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
