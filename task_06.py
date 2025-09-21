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
