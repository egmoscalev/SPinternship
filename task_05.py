import datetime

def date_in_future(integer):
  if not isinstance(integer,int):
    return datetime.datetime.now()
  date = datetime.datetime.now() + datetime.timedelta(days=integer)
  return date

print(date_in_future(2).strftime("%Y-%m-%d %H:%M:%S"))
