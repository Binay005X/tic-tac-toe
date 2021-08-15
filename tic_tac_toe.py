#---------Global Variables-------

# Game board
board = ["-", "-", "-",
         "-", "-", "-", 
         "-", "-", "-" ]

# If game is still going
game_still_going = True

# who won? or tie?
Winner = None

# Whos turn is it
Current_player = "X"

# Display board 
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tic tac toe
def play_game():

  #Display intial board
  display_board()

  while game_still_going:

    # While the game is still going
    handle_turn(Current_player)

    # handle a single turn of an aribitrary player
    check_if_game_over()

    # check if the game has ended
    flip_player()

    # The game has ended 
    
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")
 
# Handle a single turn of an aribitrary player
def handle_turn(player):

  print(player + "'s turn.")
  position = input("Choose a postion 1-9: ")
  
  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print ("You can go there. Go again.")


  board[position] = player

  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  # Set up global variables
  global winner

  # check rows
  row_winner = check_rows()
  # check columns
  column_winner = check_columns()
  # check diagonals
  diagonal_winner = check_diagonals()

  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    Winner = None
  return



def check_rows():
  # Set up global variables
  global game_still_going
  # Check if any of the rows have all the same valuee (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner (X or O)
  if row_1:
    return board[0]  
  if row_2:
    return board[3]  
  if row_3:
    return board[6]  
      
  return



def check_columns():
  # Set up global variables
  global game_still_going
  # Check if any of the columns have all the same valuee (and is not empty)
  columns_1 = board[0] == board[3] == board[6] != "-"
  columns_2 = board[1] == board[4] == board[7] != "-"
  columns_3 = board[2] == board[5] == board[8] != "-"
  # If any columns does have a match, flag that there is a win
  if columns_1 or columns_2 or columns_3:
    game_still_going = False
  # Return the winner (X or O)
  if columns_1:
    return board[0]  
  if columns_2:
    return board[1]  
  if columns_3:
    return board[2]

  return



def check_diagonals():
  # Set up global variables
  global game_still_going
  # Check if any of the columns have all the same valuee (and is not empty)
  diagonals_1 = board[0] == board[4] == board[8] != "-"
  diagonals_2 = board[6] == board[4] == board[2] != "-"
  # If any diagonals does have a match, flag that there is a win
  if diagonals_1 or diagonals_2:
    game_still_going = False
  # Return the winner (X or O)
  if diagonals_1:
    return board[0]  
  if diagonals_2:
    return board[6]  
 
  return



def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    
  return



def flip_player():
  # global variables we need 
  global Current_player
  # If Current_player was "X" then chagne it to "O"
  if Current_player == "X":
    Current_player = "O"
  # If Current_player was "O" then chagne it to "X"  
  elif Current_player == "O":
    Current_player = "X"  
  return



play_game()







# board 
# display
# play game
# handle turn
# check win
    #check win
    #check columns
    # check diagonals
# check tie
# flip player







