"""
Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
range) для определения элементов из массива list, значения которого входят в
указанный диапазон range. Если не передан хотя бы один из параметров, то
должен вернуться пустой массив.
"""

def coincidence (mylist = [],myrange = []):
  newlist = []
  for i in mylist:
    if isinstance(i,int) or isinstance (i,float):
      if i >= myrange[0] and i <= myrange[-1]:
        newlist.append(i)
  
  #print(newlist)
  return newlist

#test
coincidence([1, 2, 3, 4, 5], range(3, 6))
# => [3, 4, 5]
coincidence()
# => []
coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) # => [1, 2, 2.5]