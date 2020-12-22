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
	player_marker = ''

	while not (player_marker == 'X' or player_marker == 'O'):
		player_marker = input('Player 1: Do you want to be X or O? ').upper()

	if player_marker == 'X':
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

#check if location on board is empty
def check_space(board, position):
	if board[position] == ' ':
		return True
	else:
		return False

#promt the player to pick a location and validate if this location is available
def player_choice(board):
	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or check_space(board, position) == False:
		position = int(input('Where would you like to place you marker 1-9?'))
	return position

#function to check if there is a winner
def win_checker():
	pass

def place_marker(board, marker, position):
	board[position] = marker

