# todo
	#add alpha beta pruning 


import random
import math




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


def print_board(board):
	b = '''
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	--+-+--
	|%s|%s|%s|
	'''%(board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9])
	print(b)


def get_valid_moves(board):
	valid_moves = []
	for i in board:
		if board[i] == 'X' or board[i] == 'O':
			pass
		else:
			valid_moves.append(i)
	return valid_moves


def check_move(move, board):
	if move in range(1, 10):
		if board[move] == 'X' or board[move] == 'O':
			print('invalid move(1)')
			return False
		else:
			return True
	else:
		print('invalid move(2)')
		return False


# def make_move(mover, move):
	# board[move] = mover
	# print_board(board)
	# print('valid moves:', get_valid_moves(board))
  

# def get_move():
# 	try:
# 		move = int(input("where do you want to play?"))
# 	except:
# 		print("Invalid move")
# 		get_move()
# 	return move



def play(type, mover):
	if type == 'human':
		try:
			move = int(input("where do you want to play?"))
			if check_move(move, board) == True:
				# make_move(mover, move)
				board[move] = mover
				print_board(board)
				print('valid moves:', get_valid_moves(board))
			else:
				play(type, mover)
		except:
			print("Invalid move(0)")
			play(type, mover)

	else:
		# make_move(mover, random.choice(get_valid_moves(board)))
		best_score = -math.inf
		best_move = random.choice(get_valid_moves(board))
	
		for i in get_valid_moves(board):
			# make_move(mover, i)
			board[i] = mover
			score = minimax(mover, board, False)
			# make_move(i, i)
			board[i] = i
			if score > best_score:
				best_score = score
				best_move = i
		board[best_move] = mover
		print_board(board)
		print('valid moves:', get_valid_moves(board))




def start_game(player):
	while game_over(board)[0] == False:
		if player == 'X':
			play('human', 'X')
			if game_over(board)[0] == True:
				break
			play('ai', 'O')
			if game_over(board)[0] == True:
				break
		else:
			play('ai', 'X')
			if game_over(board)[0] == True:
				break
			play('human', 'O')
			if game_over(board)[0] == True:
				break
	if game_over(board)[1] == None:
		print('draw')
	else:
		print(game_over(board)[1], 'won')


def minimax(mover, board, ismax):
	if mover == 'X':
		opp = 'O'
	else:
		opp = 'X'

	if game_over(board)[0] == True:
		if game_over(board)[1] == None:
			return 0
		elif game_over(board)[1] == mover:
			return 1
		else:
			return -1
	else:
		if ismax == True:
			
			best_score = -math.inf
			
			for i in get_valid_moves(board):
				# make_move(mover, i)
				board[i] = mover
				score = minimax(mover, board, False)
				# make_move(i, i)
				board[i] = i
				if score > best_score:
					best_score = score
			return best_score
		else:
			best_score = math.inf
			
			for i in get_valid_moves(board):
				# make_move(opp, i)
				board[i] = opp
				score = minimax(mover, board, True)
				# make_move(i, i)
				board[i] = i
				if score < best_score:
					best_score = score
			return best_score


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
options = ('X', 'O')
player = random.choice(options)

print('you will be playing as', player)
print_board(board)
print('valid moves:', get_valid_moves(board))
start_game(player)