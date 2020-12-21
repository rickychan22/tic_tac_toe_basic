#basic implementation of the classic tiktactoe game

dic_board_val = {7: ' ', 8:'  ', 9: ' ',
				 4: ' ', 5:'  ', 6: ' ',
				 1: ' ', 2:'  ', 3: ' '	
				}

print(dic_board_val)

def board(board):
	print(board[7] + ' |' + board[8] + '|' + board[9])
	print('--+--+--')
	print(board[4] + ' |' + board[5] + '|' + board[6])
	print('--+--+--')
	print(board[1] + ' |' + board[2] + '|' + board[3])


board(dic_board_val)
