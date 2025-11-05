"""Дан список целых чисел. Необходимо разработать метод sort_list(list), который
поменяет местами все минимальные и максимальные элементы массива, а также
добавит в конец массива одно минимальное значение из него."""

def sort_list(mylist):
  
  if len(mylist) == 0:
    return []
  
  mn=min(mylist)
  mx=max(mylist)
  
  for i in range(len(mylist)):
    if mylist[i] == mn:
      mylist[i] = mx
    elif mylist[i] == mx:
      mylist[i] = mn
  mylist.append(mn)
  
  #print(mylist)
  return mylist

sort_list([])
# => []
sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
sort_list([1])
# => [1, 1]
sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]