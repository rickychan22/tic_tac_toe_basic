from board_generator import board
import game_func


def yes_no_validation():
	ready = input('Are you ready to play? Please enter Y or N').upper()

	while not (ready == 'Y' or ready == 'N'):
		ready = input('Please enter Y or N').upper()

	return ready

print('WELCOME TO THE GAME')

while True:
	#set the board to empty
	board_new = [' '] * 10

	#who goes first and set X or O
	player1_marker, player2_marker = game_func.player_input()
	turn = game_func.who_goes_first()
	print(turn + ' will go first.')

	game_on = yes_no_validation()

	if game_on == 'Y':
		play = True
	else:
		play = False

	while play:

		#player 1 turn
		if turn == 'Player 1':
			board(board_new)
			position = game_func.player_choice(board_new)
			game_func.place_marker(board_new,player1_marker,position)
			print(turn)
			
			#check if there is a win
			if game_func.win_checker(board_new, player1_marker):
				#congrats
				board(board_new)
				print('PLAYER 1 WINS')
				break
			else:
				if game_func.check_full_board(board_new):
					#tie
					board(board_new)
					print('THE GAME HAS ENDED IN A TIE')
					break
				else:
					turn = 'Player 2'
		
		#player 2 turn
		else:
			board(board_new)
			position = game_func.player_choice(board_new)
			game_func.place_marker(board_new,player2_marker,position)
			turn = 'Player 1'

			#check if there is a win
			if game_func.win_checker(board_new, player2_marker):
				#congrats
				board(board_new)
				print('PLAYER 2 WINS')
				break
			else:
				if game_func.check_full_board(board_new):
					#tie
					board(board_new)
					print('THE GAME HAS ENDED IN A TIE')
					break
				else:
					turn = 'Player 1'

	if not game_func.replay():
		break