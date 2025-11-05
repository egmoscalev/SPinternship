"""
Анаграмма — литературны при м, состоящи в перестановке букв или звуков
определ нного слова (или словосочетания), что в результате да т другое слово
или словосочетание.
Разработайте метод combine_anagrams(words_array), который принимает на вход
массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
значения при определении анаграмм.
"""

def combine_anagrams(words_array):
  
  result = {}
  
  for i in words_array:
    word = i.casefold()
    key = ''.join(sorted(word))
    result.setdefault(key, [])
    result[key].append(word)
    
  #print(list(result.values()))
  return list(result.values())


#test

combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
