import globals
import validmove
from random import randint
from copy import deepcopy

def AI_Move(GameGrid):

	ChessGrid = deepcopy(GameGrid)
	

	#static variable to keep track of depth of recursion
	#increment by 1 if not yet set else set to 1
	try:
		AI_Move.depth += 1
		# print("AI_move.depth = "+str(AI_Move.depth))
	except AttributeError :
		AI_Move.depth = 1
		# print("setting AI_move.depth = "+str(AI_Move.depth))

	#if max depth for recursion is reached then return
	if(AI_Move.depth >= globals.MAX_DEPTH):
		heuristic = getHeuristic(ChessGrid)
		# print("returning "+str(heuristic) + " depth = "+str(AI_Move.depth)+"/"+str(globals.MAX_DEPTH))
		return heuristic


	if(AI_Move.depth % 2 == 0):
		# print("AI TURN")
		turn = "2" #AI
	else:
		# print("HUMAN TURN")
		turn = "1" #human


	moves = [] #stores available moves for a piece
	heuristic = getHeuristic(ChessGrid) #stores heuristic of board state of chosen move
	makeMove = [0,0,0,0] #[fromRow,fromCol,toRow,toCol]
	noMove = True #make sure one possible move gets chosen if no move gets chosen by minimax
	checked = False #true if ai king is checked


	#check if player is checked
	if(kingChecked(ChessGrid,turn)): 
		checked = True		

	#if king not checked
	for i in range(0,8):

		for j in range(0,8):

			if(ChessGrid[i][j][0] == turn ): # 1- human(white) , 2 - AI(black)
				
				#get list of moves the piece can make
				# print("ai.py - Getting moves for "+globals.ChessGrid[i][j] + " location : "+str(i)+","+str(j))
				moves = getAllMoves(ChessGrid,i,j,ChessGrid[i][j][1],ChessGrid[i][j][0])
				# print("moves are :")
				# print(moves)
				# print()

				#for every possible move
				for move in moves:
					

					#copy grid status to new list
					# print("playing move "+str(move))
					NewChessGrid = deepcopy(ChessGrid)
					NewChessGrid[i][j] = "0"
					NewChessGrid[move[0]][move[1]] = ChessGrid[i][j]
					#print("New Grid :")
					#PrintGrid(NewChessGrid)

					#if ai was previously checked and after the move is still checked then don't allow the move
					if(checked and kingChecked(NewChessGrid,turn)):
						continue;

					#perform MINIMAX/ALPHA-BETA
					moveHeuristic = AI_Move(NewChessGrid)

					#reduce depth value when returning from recursion
					AI_Move.depth -= 1

					# print("back checking "+ChessGrid[i][j] + " depth = "+str(AI_Move.depth))
					
					#if heuristic is same chose generated move by a chance
					if(moveHeuristic == heuristic):
						xyz = randint(1,100)
						if(xyz > 50):
							moveHeuristic = heuristic
							makeMove = [i,j,move[0],move[1]]

					#if better heuristic from move choose this move
					#turn values AI - 1, HUMAN - 2
					#AI will choose a larger heuristic value (MAX)
					#human will choose a lower heuristic value (MIN)
					if(moveHeuristic > heuristic and turn == "1"):
						heuristic = moveHeuristic 
					if(moveHeuristic < heuristic and turn == "2"):
						heuristic = moveHeuristic 

	return heuristic



#calculate and return heuristic of the board
def getHeuristic(ChessGrid):
	
	whiteVal = 0
	blackVal = 0
	for i in range(0,8):
		for j in range(0,8):

			#empty
			if(ChessGrid[i][j] == "0"):
				continue

			#pawn
			if(ChessGrid[i][j][1] == "1"):
				if(ChessGrid[i][j][0] == "1"):
					whiteVal += 1
				else:
					blackVal += 1
			#rook
			elif(ChessGrid[i][j][1] == "2"):
				if(ChessGrid[i][j][0] == "1"):
					whiteVal += 2
				else:
					blackVal += 2
			#bishop
			elif(ChessGrid[i][j][1] == "3"):
				if(ChessGrid[i][j][0] == "1"):
					whiteVal += 3
				else:
					blackVal += 3
			#knight
			elif(ChessGrid[i][j][1] == "4"):
				if(ChessGrid[i][j][0] == "1"):
					whiteVal += 4
				else:
					blackVal += 4
			#queen
			elif(ChessGrid[i][j][1] == "5"):
				if(ChessGrid[i][j][0] == "1"):
					whiteVal += 5
				else:
					blackVal += 5
			#king
			elif(ChessGrid[i][j][1] == "6"):
				if(ChessGrid[i][j][0] == "1"):
					whiteVal += 6
				else:
					blackVal += 6

	if(kingChecked(ChessGrid,"1")):
		blackVal += 100;

	if(kingChecked(ChessGrid,"2")):
		whiteVal += 100;

	return whiteVal - blackVal



#check's if the location is empty or occupied by enemy
def CheckCell(ChessGrid,row,col,color):

	if(row < 0 or col < 0 or row > 7 or col > 7):
		return False

	try:
		#if cell is empty or occupied by opponent
		if(ChessGrid[row][col][0]  == "0" or ChessGrid[row][col][0] != color):
			return True
		#else space is occupied by own piece
		return False
	except IndexError: #catch IndexError
		return False


def getAllMoves(ChessGrid,row,col,piece,color):

	moves = []

	#Pawn
	if(piece == "1"):

		#separate if else for black and white since black pawns will only go downwards
		#and white pawns only upwards
		if(color == "2"):  #black
			#initial 2 step
			if( row == 1 and ChessGrid[row+2][col] == "0"):
				moves.append([row+2,col])
			#moving a step
			if( ChessGrid[row+1][col] == "0" ):
				moves.append([row+1,col])
			#attacking
			if( row+1 < 8 and col + 1 < 8 and ChessGrid[row+1][col+1][0] == "1" ):
				moves.append([row+1,col+1])
			if( row+1 < 8 and col - 1 >= 0 and ChessGrid[row+1][col-1][0] == "1" ):
				moves.append([row+1,col-1])

		else: #white
			#initial 2 step
			if( row == 6 and ChessGrid[row-2][col] == "0"):
				moves.append([row-2,col])
			#moving a step
			if( ChessGrid[row-1][col] == "0" ):
				moves.append([row-1,col])
			#attacking
			if( row-1 >= 0 and col + 1 < 8 and ChessGrid[row-1][col+1][0] == "2" ):
				moves.append([row-1,col+1])
			if( row-1 >= 0 and col - 1 >= 0 and ChessGrid[row-1][col-1][0] == "2" ):
				moves.append([row-1,col-1])


	#Rook or Queen
	#Queen can move up/down/left/right like a Rook
	if(piece == "2" or piece == "5"):

		#going down
		i = row + 1
		while (i<=7):
			#empty square in path
			if(ChessGrid[i][col][0] == "0"):
				moves.append([i,col])

			#opponent in path
			elif(ChessGrid[i][col][0] != color):
				moves.append([i,col])
				break

			#own piece in path
			elif(ChessGrid[i][col][0] == color):
				break
			i+=1

		#going up
		i = row - 1
		while (i>=0):

			if(ChessGrid[i][col][0] == "0"):
				moves.append([i,col])

			elif(ChessGrid[i][col][0] != color):
				moves.append([i,col])
				break

			elif(ChessGrid[i][col][0] == color):
				break
			i-=1

		#going left
		j = col - 1
		while (j>=0):
			if(ChessGrid[row][j][0] == "0"):
				moves.append([row,j])

			elif(ChessGrid[row][j][0] != color):
				moves.append([row,j])
				break

			elif(ChessGrid[row][j][0] == color):
				break
			j-=1

		#going right
		j = col + 1
		while (j<=7):
			if(ChessGrid[row][j][0] == "0"):
				moves.append([row,j])

			elif(ChessGrid[row][j][0] != color):
				moves.append([row,j])
				break

			elif(ChessGrid[row][j][0] == color):
				break
			j+=1

	#Bishop or Queen
	#queen can move diagonally like the bishop
	if(piece == "3" or piece == "5"):

		#going up right
		i = row - 1 
		j = col + 1
		while (i>=0 and j<=7):

			#empty space in path
			if(ChessGrid[i][j][0] == "0"):
				moves.append([i,j])
			#opponent in path
			elif(ChessGrid[i][j][0] != color):
				moves.append([i,j])
				break
			#own piece in path
			elif(ChessGrid[i][j][0] == color):
				break
			i-=1
			j+=1

		#going down right
		i = row + 1
		j = col + 1
		while (i<=7 and j<=7):
			if(ChessGrid[i][j][0] == "0"):
				moves.append([i,j])
			elif(ChessGrid[i][j][0] != color):
				moves.append([i,j])
				break
			elif(ChessGrid[i][j][0] == color):
				break		
			i+=1
			j+=1

		#going down left
		i = row + 1
		j = col - 1
		while (i<=7 and j>=0 ):
			if(ChessGrid[i][j][0] == "0"):
				moves.append([i,j])
			elif(ChessGrid[i][j][0] != color):
				moves.append([i,j])
				break
			elif(ChessGrid[i][j][0] == color):
				break	
			i+=1
			j-=1

		#going up left
		i = row - 1
		j = col - 1
		while (i>=0 and j>=0 ):
			if(ChessGrid[i][j][0] == "0"):
				moves.append([i,j])
			elif(ChessGrid[i][j][0] != color):
				moves.append([i,j])
				break
			elif(ChessGrid[i][j][0] == color):
				break	
			i-=1
			j-=1

	#Knight
	if(piece == "4"):

		if(CheckCell(ChessGrid,row+2,col+1,color)):
			moves.append([row+2,col+1])

		if(CheckCell(ChessGrid,row+2,col-1,color)):
			moves.append([row+2,col-1])

		if(CheckCell(ChessGrid,row-2,col+1,color)):
			moves.append([row-2,col+1])

		if(CheckCell(ChessGrid,row-2,col-1,color)):
			moves.append([row-2,col-1])

		if(CheckCell(ChessGrid,row+1,col+2,color)):
			moves.append([row+1,col+2])

		if(CheckCell(ChessGrid,row-1,col+2,color)):
			moves.append([row-1,col+2])

		if(CheckCell(ChessGrid,row+1,col-2,color)):
			moves.append([row+1,col-2])

		if(CheckCell(ChessGrid,row-1,col-2,color)):
			moves.append([row-1,col-2])

	#King
	if(piece == "6"):

		if(CheckCell(ChessGrid,row+1,col,color)):
			moves.append([row+1,col])

		if(CheckCell(ChessGrid,row+1,col+1,color)):
			moves.append([row+1,col+1])

		if(CheckCell(ChessGrid,row+1,col-1,color)):
			moves.append([row+1,col-1])

		if(CheckCell(ChessGrid,row,col-1,color)):
			moves.append([row,col-1])

		if(CheckCell(ChessGrid,row,col+1,color)):
			moves.append([row,col+1])

		if(CheckCell(ChessGrid,row-1,col-1,color)):
			moves.append([row-1,col-1])

		if(CheckCell(ChessGrid,row-1,col,color)):
			moves.append([row-1,col])

		if(CheckCell(ChessGrid,row-1,col+1,color)):
			moves.append([row-1,col+1])

	# print(moves)
	return moves


def kingChecked(ChessGrid,color):

	kingRow  = None
	kingCol = None
	# print('color '+color)
	for row in range(0,8) :
		for col in range(0,8):

			if(ChessGrid[row][col][0] == color and ChessGrid[row][col][1] == '6'):
				kingRow = row
				kingCol = col


	for row in range(0,8) :
		for col in range(0,8):

			if(ChessGrid[row][col][0] != color and ChessGrid[row][col] != '0'):

				moves = getAllMoves(ChessGrid,row,col,ChessGrid[row][col][1],ChessGrid[row][col][0])

				if([kingRow,kingCol] in moves):
					return True

	return False


