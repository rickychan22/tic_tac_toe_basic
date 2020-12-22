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

#place marker on the board
def place_marker(board, marker, position):
	board[position] = marker

#check if board is full ie if full and no winner then it is a tie
def check_full_board(board):
	for i in range (0,10):
		if check_space(board, i):
			return False
	return True


#function to check if there is a winner
def win_checker(board, mark):
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

#break while loop if players do not want to continue 
def replay():
	play_again = input('Would you like to play again, Yes or No?').upper()

	if player_again == 'YES':
		return True
	else:
		return False



