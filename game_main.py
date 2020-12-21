from board_generator import board
import game_func

print('WELCOME TO THE GAME')


while True:
	#set the board to empty
	board_new = [' '] * 10
	player1_marker = game_func.player_input()
	turn = game_func.who_goes_first()
	print(turn + ' will go first.')