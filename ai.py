import globals
import validmove
from random import randint
from copy import deepcopy

def AI_Move(GameGrid):

	ChessGrid = deepcopy(GameGrid)
	

	#static variable to keep track of depth of recursio
	try:
		AI_Move.depth += 1
		print("AI_move.depth = "+str(AI_Move.depth))
	except AttributeError :
		AI_Move.depth = 1
		print("setting AI_move.depth = "+str(AI_Move.depth))

	if(AI_Move.depth >= globals.MAX_DEPTH):
		tempVal = getHeuristic(ChessGrid)
		print("returning "+str(tempVal) + " depth = "+str(AI_Move.depth)+"/"+str(globals.MAX_DEPTH))
		return tempVal

	if(AI_Move.depth % 2 == 0):
		print("AI TURN")
		turn = "2" #AI
	else:
		print("HUMAN TURN")
		turn = "1" #human

	heuristic = 0

	#if king checked
	#TODO
	pass


	#if king not checked
	for i in range(0,8):

		for j in range(0,8):

			if(ChessGrid[i][j][0] == turn ): #1 - AI .. 2 - human
				
				#if the piece belongs to the computer get a list of all possible moves
				#the piece can make
				print("ai.py - Getting moves for "+globals.ChessGrid[i][j] + " location : "+str(i)+","+str(j))
				moves = getAllMoves(ChessGrid,i,j,ChessGrid[i][j][1],ChessGrid[i][j][0])
				print("moves are :")
				print(moves)
				print()
				for move in moves:
					
					print("playing move "+str(move))
					NewChessGrid = deepcopy(ChessGrid)
					NewChessGrid[i][j] = "0"
					NewChessGrid[move[0]][move[1]] = ChessGrid[i][j]
					#print("New Grid :")
					#PrintGrid(NewChessGrid)
					moveHeuristic = AI_Move(NewChessGrid)
					AI_Move.depth -= 1
					print("back checking "+ChessGrid[i][j] + " depth = "+str(AI_Move.depth))
					#if heuristic is same chose generated move by a chance
					if(moveHeuristic == heuristic):
						xyz = randint(1,100)
						if(xyz > 50):
							moveHeuristic = heuristic
							makeMove = [i,j,move[0],move[1]]
					#if better heuristic from move choose this move
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


	return whiteVal - blackVal



#check's if the location is empty or occupied by enemy
def CheckMove(ChessGrid,row,col,color):

	if(row < 0 or col < 0 or row > 7 or col > 7):
		return False

	try:
		if(ChessGrid[row][col][0]  == "0" or ChessGrid[row][col][0] != color):
			return True
		return False
	except IndexError: #catch IndexError
		return False


def getAllMoves(ChessGrid,row,col,piece,color):

	moves = []

	#Pawn
	if(piece == "1"):
		
		if(color == "2"):
			#moving a step
			if( ChessGrid[row+1][col] == "0" ):
				moves.append([row+1,col])
			#attacking
			if( row+1 < 8 and col + 1 < 8 and ChessGrid[row+1][col+1][0] == "1" ):
				moves.append([row+1,col+1])
			if( row+1 < 8 and col - 1 > 0 and ChessGrid[row+1][col-1][0] == "1" ):
				moves.append([row+1,col-1])
		else:
			if( ChessGrid[row-1][col] == "0" ):
				moves.append([row-1,col])
			if( row+1 < 8 and col + 1 < 8 and ChessGrid[row-1][col+1][0] == "2" ):
				moves.append([row-1,col+1])
			if( row+1 < 8 and col - 1 > 0 and ChessGrid[row-1][col-1][0] == "2" ):
				moves.append([row-1,col-1])


	#Rook or Queen
	if(piece == "2" or piece == "5"):

		#going down
		i = row + 1
		while (i<=7):
			if(ChessGrid[i][col][0] == "0"):
				moves.append([i,col])

			elif(ChessGrid[i][col][0] != color):
				moves.append([i,col])
				break

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
	if(piece == "3" or piece == "5"):

		#going up right
		i = row - 1 
		j = col + 1
		while (i>=0 and j<=7):
			if(ChessGrid[i][j][0] == "0"):
				moves.append([i,j])
			elif(ChessGrid[i][j][0] != color):
				moves.append([i,j])
				break
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

		if(CheckMove(ChessGrid,row+2,col+1,color)):
			moves.append([row+2,col+1])

		if(CheckMove(ChessGrid,row+2,col-1,color)):
			moves.append([row+2,col-1])

		if(CheckMove(ChessGrid,row-2,col+1,color)):
			moves.append([row-2,col+1])

		if(CheckMove(ChessGrid,row-2,col-1,color)):
			moves.append([row-2,col-1])

		if(CheckMove(ChessGrid,row+1,col+2,color)):
			moves.append([row+1,col+2])

		if(CheckMove(ChessGrid,row-1,col+2,color)):
			moves.append([row-1,col+2])

		if(CheckMove(ChessGrid,row+1,col-2,color)):
			moves.append([row+1,col-2])

		if(CheckMove(ChessGrid,row-1,col-2,color)):
			moves.append([row-1,col-2])

	#King
	if(piece == "6"):

		if(CheckMove(ChessGrid,row+1,col,color)):
			moves.append([row+1,col])

		if(CheckMove(ChessGrid,row+1,col+1,color)):
			moves.append([row+1,col+1])

		if(CheckMove(ChessGrid,row+1,col-1,color)):
			moves.append([row+1,col-1])

		if(CheckMove(ChessGrid,row,col-1,color)):
			moves.append([row,col-1])

		if(CheckMove(ChessGrid,row,col+1,color)):
			moves.append([row,col+1])

		if(CheckMove(ChessGrid,row+1,col-1,color)):
			moves.append([row+1,col-1])

		if(CheckMove(ChessGrid,row+1,col,color)):
			moves.append([row+1,col])

		if(CheckMove(ChessGrid,row+1,col+1,color)):
			moves.append([row+1,col+1])

	return moves