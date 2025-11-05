"""
Разработать методы для программы Камень-Ножницы-Бумага. При реализации
обработки исключений важно не использовать встроенные классы ошибок с
передачей им сообщения, а разработать классы с представленными ниже
названиями.
Метод rps_game_winner должен принимать на вход массив следующей структуры
[ ["player1", "P"], ["player2", "S"] ], где P — бумага, S — ножницы, R — камень, и
функционировать следующим образом:
• если количество игроков больше 2 необходимо вызывать исключение
WrongNumberOfPlayersError
• если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
исключение NoSuchStrategyError
• в иных случаях необходимо вернуть имя и ход победителя, если оба
игрока походили одинаково - выигрывает первый игрок.
"""



class WrongNumberOfPlayersError(Exception):
  pass

class NoSuchStrategyError(Exception):
  pass

def rps_game_winner(mylist):
  
  if (len(mylist) > 2):
    raise WrongNumberOfPlayersError
    
  winner = mylist[0]
  
  for i in mylist:
    if (i[1] not in ['R','P','S']):
      raise NoSuchStrategyError
  
  if (mylist[0][1] == 'P' and mylist[1][1] == 'S' or mylist[0][1] == 'S' and mylist[1][1] == 'R' or mylist[0][1] == 'R' and mylist[1][1] == 'P'):
    winner = mylist[1]
  
  return winner
  

#test
for i in ['R','P','S']:
  for j in ['R','P','S']:
    print(i, 'vs', j)
    print('winner is',rps_game_winner([['player1',i],['player2',j]]))
