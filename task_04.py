def sort_list(mylist):
  
  if len(mylist) == 0:
    return mylist
  
  mn=min(mylist)
  mx=max(mylist)
  
  for i in range(len(mylist)):
    if mylist[i] == mn:
      mylist[i] = mx
    elif mylist[i] == mx:
      mylist[i] = mn
  mylist.append(mn)
  
  return mylist
