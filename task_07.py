def combine_anagrams(words_array):
  
  result = {}
  
  for i in words_array:
    word = i.casefold()
    key = ''.join(sorted(word))
    result.setdefault(key, [])
    result[key].append(word)
    
  print(list(result.values()))


#test

combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
