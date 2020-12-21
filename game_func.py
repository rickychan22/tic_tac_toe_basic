from board_generator import board
import random

'''

select which marker the player wants to be 

p1 picks location for marker
check if location is available if not then prompt user to pick a new location
if available place the respected marker on the board
set turn to player 2 and repeat

'''

dic_board_val = {7: ' ', 8:' ', 9: ' ',
				 4: ' ', 5:' ', 6: ' ',
				 1: ' ', 2:' ', 3: ' '	
				}

#promt the user if they want to be X or O
def player_input():
	player_choice = ''

	while not (player_choice == 'X' or player_choice =='O'):
		player_choice  = input('Player1: Would you like to be X or O?').upper()

	if player_choice == 'X':
		return ('X','O')
	else:
		return ('O','X')

#determine which play will go first
def who_goes_first():
	random_num = random.randint(0,1)

	if random_num == 0:
		return 'Player 1'
	else:
		return 'Player 2'

#function to check if there is a winner
def win_checker():
	pass

def place_marker(board, marker, position):
	board[position] = marker

