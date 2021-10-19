# todo
	# remove redundant code
	# rework base x & o logic and remove unnecessary functions
	# add comments


import random
import math


# game_over checks whether the game has ended and returns the winner
def game_over(board):
	if board[1] == board[2] == board[3]:
		winner = board[1]
		return True, winner
	elif board[4] == board[5] == board[6]:
		winner = board[4]
		return True, winner
	elif board[7] == board[8] == board[9]:
		winner = board[7]
		return True, winner
	elif board[1] == board[4] == board[7]:
		winner = board[1]
		return True, winner
	elif board[2] == board[5] == board[8]:
		winner = board[2]
		return True, winner
	elif board[3] == board[6] == board[9]:
		winner = board[3]
		return True, winner
	elif board[1] == board[5] == board[9]:
		winner = board[1]
		return True, winner
	elif board[3] == board[5] == board[7]:
		winner = board[3]
		return True, winner
	elif get_valid_moves(board) == []:
		winner = None
		return True, winner
	else:
		winner = None
		return False, winner


# print_board prints the current state of the game board
def print_board(board):
	b = '''
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	'''%(board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9])
	print(b)


# get_valid_moves returns a list of all valid moves for the current  board state
def get_valid_moves(board):
	valid_moves = []
	for i in board:
		if board[i] == 'X' or board[i] == 'O':
			pass
		else:
			valid_moves.append(i)
	return valid_moves


# def check_move(move, board):
	# if move in range(1, 10):
	# 	if board[move] == 'X' or board[move] == 'O':
	# 		print('invalid move(1)')
	# 		return False
	# 	else:
	# 		return True
	# else:
	# 	print('invalid move(2)')
	# 	return False

def check_move(move, board):
	if move in get_valid_moves(board):
		return True
	else:
		print('invalid move')
		# print('invalid move: from check_move(move, board)')
		return False


# def make_move(mover, move):
	# board[move] = mover
	# print_board(board)
	# print('valid moves:', get_valid_moves(board))
  

# def get_move():
	# try:
		# move = int(input("where do you want to play?"))
	# except:
		# print("Invalid move")
		# get_move()
	# return move



def play(is_human, human, ai, board):
	if is_human == True:
		try:
			move = int(input('where do you want to play %s?'%human))
			if check_move(move, board) == True:
				board[move] = human
				print_board(board)
				print('valid moves:', get_valid_moves(board))
			else:
				play(is_human, human, board)
		except:
			print("Invalid move(0)")
			play(is_human, human, ai, board)
	else:
	# random move:
		# board[random.choice(get_valid_moves(board))] = ai

	# WARNING: i havent updated the minimax function. it WILL break things if uncommented.
	# best move found using minimax:
		# best_score = -math.inf
		# best_move = random.choice(get_valid_moves(board))
	
		# for i in get_valid_moves(board):
		# 	# make_move(mover, i)
		# 	board[i] = mover
		# 	score = minimax(mover, board, False)
		# 	# make_move(i, i)
		# 	board[i] = i
		# 	if score > best_score:
		# 		best_score = score
		# 		best_move = i
		# board[best_move] = mover
		# print_board(board)
		# print('valid moves:', get_valid_moves(board))

	# best move found using minimax and aplha beta pruning:
		best_score = -math.inf
		best_move = random.choice(get_valid_moves(board))
	
		for i in get_valid_moves(board):
			board[i] = ai
			score = minimax_abp(ai, human, board, False, -math.inf, math.inf)
			board[i] = i
			if score > best_score:
				best_score = score
				best_move = i
		board[best_move] = ai
		print_board(board)
		print('the ai played', ai, 'at', best_move)
		print('valid moves:', get_valid_moves(board))




def start_game(human, ai, board):
	while game_over(board)[0] == False:
		if human == 'X':
			play(True, human, ai, board)
			if game_over(board)[0] == True:
				break
			play(False, human, ai, board)
			if game_over(board)[0] == True:
				break
		else:
			play(False, human, ai, board)
			if game_over(board)[0] == True:
				break
			play(True, human, ai, board)
			if game_over(board)[0] == True:
				break
	if game_over(board)[1] == None:
		print('draw')
	else:
		print(game_over(board)[1], 'won')

# WARNING: The minimax function hasent been updated. it WILL break things if uncommented. 
# def minimax(mover, board, ismax):
	# if mover == 'X':
	# 	opp = 'O'
	# else:
	# 	opp = 'X'

	# if game_over(board)[0] == True:
	# 	if game_over(board)[1] == None:
	# 		return 0
	# 	elif game_over(board)[1] == mover:
	# 		return 1
	# 	else:
	# 		return -1
	# else:
	# 	if ismax == True:
	# 		best_score = -math.inf
			
	# 		for i in get_valid_moves(board):
	# 			# make_move(mover, i)
	# 			board[i] = mover
	# 			score = minimax(mover, board, False)
	# 			# make_move(i, i)
	# 			board[i] = i
	# 			if score > best_score:
	# 				best_score = score
	# 		return best_score
	# 		# best_score = max(best_score, score)
	# 		# return max(best_score, score)

	# 	else:
	# 		best_score = math.inf
			
	# 		for i in get_valid_moves(board):
	# 			# make_move(opp, i)
	# 			board[i] = opp
	# 			score = minimax(mover, board, True)
	# 			# make_move(i, i)
	# 			board[i] = i
	# 			if score < best_score:
	# 				best_score = score
	# 		return best_score
	# 		# best_score = min(best_score, score)
	# 		# return min(best_score, score)



def minimax_abp(ai, human, board, ismax, alpha, beta):
	if game_over(board)[0] == True:
		if game_over(board)[1] == None:
			return 0
		elif game_over(board)[1] == ai:
			return 1
		else:
			return -1
	else:
		if ismax == True:
			best_score = -math.inf
			
			for i in get_valid_moves(board):
				board[i] = ai
				# only print the board if you want to see every move tried. might take time.
				# print_board(board)
				score = minimax_abp(ai, human, board, False, alpha, beta)
				board[i] = i
				if score > best_score:
					best_score = score
				if best_score > alpha:
					alpha = best_score
				if alpha >= beta:
					break
			return best_score
		else:
			best_score = math.inf
			
			for i in get_valid_moves(board):
				board[i] = human
				# only print the board if you want to see every move tried. might take time.
				# print_board(board)
				score = minimax_abp(ai, human, board, True, alpha, beta)
				board[i] = i
				if score < best_score:
					best_score = score
				if best_score < beta:
					beta = best_score
				if alpha >= beta:
					break
			return best_score


def main():
# dictionary 'board' represents the main tictactoe board 
	board = {
		1: 1,
		2: 2,
		3: 3,
		4: 4,
		5: 5,
		6: 6,
		7: 7,
		8: 8,
		9: 9
	}
# 'X' and 'O' are randomly assigned
	options = ('X', 'O')
	human = random.choice(options)
	if human == 'X':
		ai = 'O'
	else:
		ai = 'X'

	print('you will be playing as', human)
	print_board(board)
	print('valid moves:', get_valid_moves(board))
	start_game(human, ai, board)


if __name__ == '__main__':
	main()