"""
Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
переданных словаря, значениями ключей в которых являются числа, и вернет
новый словарь, полученный по следующим правилам:
• приоритетными являются ключи того словаря, сумма значений ключей
которого больше (если суммы значений ключей будут равны, то второй
словарь считается более приоритетным) DONE
• ключи со значениями меньше 10 не должны попасть в финальный
словарь (ключи и значения в примере перепутаны?)
• получившийся словарь должен вернуться упорядоченным по значениям
ключей в порядке возрастания.
Тесты для примеров и проверки: 

connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })
# =>
{ "c": 11, "b": 12 }
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) # =>
{ d: 11, "c": 12, "a": 13 }
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })
# =>
{ "c": 11, "b": 12, "a": 15 }

"""



def connect_dicts(dict1,dict2):
  
  if (sum(dict1.values()) > sum(dict2.values())):
    #dict 1 is prioritized
    
    dict1 = {key:val for key, val in dict1.items() if val >= 10}

    dict2 = {key:val for key, val in dict2.items() if key not in dict1.keys() and val >= 10}

    dict2.update(dict1)

    dict2 = dict(sorted(dict2.items(), key = lambda item: item[1] ))
    
    #print(dict2)
    return dict2
    
    
  else:
    #dict 2 is prioritized
    
    dict2 = {key:val for key, val in dict2.items() if val >= 10}

    dict1 = {key:val for key, val in dict1.items() if key not in dict2.keys() and val >= 10}

    dict1.update(dict2)

    dict1 = dict(sorted(dict1.items(), key = lambda item: item[1] ))
    
    
    #print(dict1)
    return dict1
  

  
#test

connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })
# =>{ "c": 11, "b": 12 }
connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }) 
# =>{ d: 11, "c": 12, "a": 13 }
connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })
# =>{ "c": 11, "b": 12, "a": 15 }



