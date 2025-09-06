def coincidence (mylist,myrange):
  newlist = []
  for i in mylist:
    if i in myrange:
      newlist.append(i)
  
  
  return newlist
