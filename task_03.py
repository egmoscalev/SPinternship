def max_odd(mylist):
  n = None
  for i in mylist:
    if isinstance(i,int) or (isinstance(i,float) and i % 1 == 0):
      if i % 2 != 0:
        if n == None or n < i:
          n = int(i)
      
  return n
