import globals

def validMove(fromRow,fromColumn,toRow,toColumn,Piece):

	#WhitePawn moving
	if( (Piece == "11" and toColumn == fromColumn and fromRow == 6 and (toRow == 4 or toRow == 5)) or (Piece == "11" and toColumn == fromColumn and (toRow + 1 == fromRow)) ): #path is clear
		if(globals.ChessGrid[toRow][toColumn][0] == "2"  or globals.ChessGrid[toRow][toColumn][0] == "1" ): #path is blocked
			return False
		globals.ChessGrid[toRow][toColumn] = "11"
		globals.ChessGrid[fromRow][fromColumn] = "0"
		return True

	#BlackPawn moving
	if( (Piece == "21" and toColumn == fromColumn and fromRow == 1 and (toRow == 2 or toRow == 3)) or (Piece == "21" and toColumn ==fromColumn and (fromRow + 1 == toRow )) ): #path is clear
		if(globals.ChessGrid[toRow][toColumn][0] == "2"  or globals.ChessGrid[toRow][toColumn][0] == "1" ): #path blocked
			return False
		globals.ChessGrid[toRow][toColumn] = "21"
		globals.ChessGrid[fromRow][fromColumn] = "0"
		return True

	#WhitePawn attacking
	if( Piece == "11" and (abs(toColumn-fromColumn) == 1) and (toRow + 1 == fromRow) and globals.ChessGrid[toRow][toColumn][0] == "2"):
		globals.ChessGrid[toRow][toColumn] = "11"
		globals.ChessGrid[fromRow][fromColumn] = "0"
		return True
	
	#BlackPawn attacking
	if( Piece == "21" and (abs(toColumn-fromColumn) == 1) and (toRow == fromRow + 1) and globals.ChessGrid[toRow][toColumn][0] == "1"):
		globals.ChessGrid[toRow][toColumn] = "21"
		globals.ChessGrid[fromRow][fromColumn] = "0"
		return True

	#WhiteRook
	if( Piece == "12" and (toColumn == fromColumn or toRow == fromRow) ): #path is valid
		if(RookPathClear(fromRow,fromColumn,toRow,toColumn)): #check for clear path
			globals.ChessGrid[toRow][toColumn] = "12"
			globals.ChessGrid[fromRow][fromColumn] = "0"
			return True	
		return False

	#BlackRook
	if( Piece == "22" and (toColumn == fromColumn or toRow == fromRow) ):
		if(RookPathClear(fromRow,fromColumn,toRow,toColumn)): #check for clear path
			globals.ChessGrid[toRow][toColumn] = "22"
			globals.ChessGrid[fromRow][fromColumn] = "0"
			return True		
		return False


	#WhiteBishop
	if( Piece == "13" and (abs(toRow - fromRow) == abs(toColumn - fromColumn)) ):
		if(BishopPathClear(fromRow,fromColumn,toRow,toColumn)):
			globals.ChessGrid[toRow][toColumn] = "13"
			globals.ChessGrid[fromRow][fromColumn] = "0"
			return True	
		return False

	#BlackBishop
	if( Piece == "23" and (abs(toRow - fromRow) == abs(toColumn - fromColumn)) ):
		if(BishopPathClear(fromRow,fromColumn,toRow,toColumn)):
			globals.ChessGrid[toRow][toColumn] = "23"
			globals.ChessGrid[fromRow][fromColumn] = "0"
			return True	
		return False


	#WhiteKnight
	if( Piece == "14" and ( ((abs(toRow - fromRow) == 2) and (abs(toColumn - fromColumn) == 1)) or ((abs(toRow - fromRow) == 1) and (abs(toColumn - fromColumn) == 2)) ) ):
		globals.ChessGrid[toRow][toColumn] = "14"
		globals.ChessGrid[fromRow][fromColumn] = "0"
		return True	

	#BlackKnight
	if( Piece == "24" and ( ((abs(toRow - fromRow) == 2) and (abs(toColumn - fromColumn) == 1)) or ((abs(toRow - fromRow) == 1) and (abs(toColumn - fromColumn) == 2)) ) ):
		globals.ChessGrid[toRow][toColumn] = "24"
		globals.ChessGrid[fromRow][fromColumn] = "0"
		return True	

	#WhiteQueen
	if( Piece == "15" and ( (abs(toRow - fromRow) == abs(toColumn - fromColumn)) or (toRow == fromRow) or (toColumn == fromColumn) )):
		if(QueenPathClear(fromRow,fromColumn,toRow,toColumn)):
			globals.ChessGrid[toRow][toColumn] = "15"
			globals.ChessGrid[fromRow][fromColumn] = "0"
			return True	
		return False

	#BlackQueen	
	if( Piece == "25" and ( (abs(toRow - fromRow) == abs(toColumn - fromColumn)) or (toRow == fromRow) or (toColumn == fromColumn) )):
		if(QueenPathClear(fromRow,fromColumn,toRow,toColumn)):
			globals.ChessGrid[toRow][toColumn] = "25"
			globals.ChessGrid[fromRow][fromColumn] = "0"
			return True	
		return False

	#WhiteKing
	if( Piece == "16" and ( (abs(toRow - fromRow) <=1) and (abs(toColumn - fromColumn) <= 1)  )):
		globals.ChessGrid[toRow][toColumn] = "16"
		globals.ChessGrid[fromRow][fromColumn] = "0"
		return True	

	#BlackKing
	if( Piece == "26" and ( (abs(toRow - fromRow) <=1) and (abs(toColumn - fromColumn) <= 1)  )):
		globals.ChessGrid[toRow][toColumn] = "26"
		globals.ChessGrid[fromRow][fromColumn] = "0"
		return True	
		
	return False

#following functions check if the paths are not obstructed by another piece
def RookPathClear(fromRow,fromColumn,toRow,toColumn):
	
	if(toColumn == fromColumn): 
		low = min(toRow,fromRow) + 1	#select from and to indices and skip to and from indices
		high = max(toRow,fromRow) - 1
		for i in range(low,high+1):
			if(globals.ChessGrid[i][fromColumn] != "0"):
				return False

	if(toRow == fromRow):
		low = min(toColumn,fromColumn) + 1	#select from and to indices and skip to and from indices
		high = max(toColumn,fromColumn) - 1 
		for j in range(low,high+1):
			if(globals.ChessGrid[toRow][j] != "0"):
				return False

	return True

def BishopPathClear(fromRow,fromColumn,toRow,toColumn):
	
	if(fromRow < toRow):	#if to locations is above
		rowInc = 1 			#row index will be incremented
		row = fromRow + 1 	
	else:
		rowInc = -1 		#row index will be decremented
		row = fromRow - 1 

	if(fromColumn < toColumn): #if to location is to the right
		colInc = 1 			   #col index will be incremented	
		col = fromColumn + 1
	else:
		colInc = -1 		   #col index will be decremented
		col = fromColumn - 1

	while not(row == toRow and col == toColumn): #check path incrementing row and col
		if(globals.ChessGrid[row][col] != "0"):
			return False
		row += rowInc
		col += colInc

	return True


def QueenPathClear(fromRow,fromColumn,toRow,toColumn):
	return BishopPathClear(fromRow,fromColumn,toRow,toColumn) or RookPathClear(fromRow,fromColumn,toRow,toColumn) #Rook + Bishop = Queen