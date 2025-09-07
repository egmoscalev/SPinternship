def coincidence (mylist,myrange):
  newlist = []
  for i in mylist:
    if isinstance(i,int) or isinstance (i,float):
      if i >= myrange[0] and i <= myrange[-1]:
        newlist.append(i)
  
  return newlist
