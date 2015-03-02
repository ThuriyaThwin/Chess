
from Tkinter import *
import globals
import validmove
import ai
from random import randint
from copy import deepcopy


#uncomment for logging to file
#old_stdout = sys.stdout
#log_file = open("message.log","w")
#sys.stdout = log_file

#TODO
#ai sucks
#add checkmate

class MainWindow(Frame):

	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent = parent
		self.init()

	#initialize the GUI frames and grids
	def init(self):

		self.MenuBar = Frame(self.parent,background="blue")
		self.MenuBar.pack()

		self.NewGameButton = Button(self.MenuBar,text="New Game")
		self.NewGameButton.pack()

		self.BlackPiecesFrame = Frame(self.parent,background="red")
		self.BlackPiecesFrame.pack()
		
		self.ChessGridFrame = Frame(self.parent,background="pink")
		self.ChessGridFrame.pack()

		self.CreateGrid()

		self.WhitePiecesFrame = Frame(self.parent,background="red")
		self.WhitePiecesFrame.pack()
		
		

	#create initial chess grid configuration
	def CreateGrid(self):
		
		self.ChessCells = []

		for i in range(0,8):
			self.ChessCells.append([])
			globals.ChessGrid.append([])
			for j in range(0,8):		
				if((i==0 and j==0) or (i==0 and j==7)):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["BlackRook"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("22")
					self.ChessCells[i][j].grid(row=i,column=j)
			
				elif((i==0 and j==1) or (i==0 and j==6)):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["BlackKnight"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("24")
					self.ChessCells[i][j].grid(row=i,column=j)

				elif((i==0 and j==2) or (i==0 and j==5)):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["BlackBishop"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("23")
					self.ChessCells[i][j].grid(row=i,column=j)

				elif(i==0 and j==3):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["BlackKing"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("26")
					self.ChessCells[i][j].grid(row=i,column=j)

				elif(i==0 and j==4):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["BlackQueen"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("25")
					self.ChessCells[i][j].grid(row=i,column=j)

				elif(i==1):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["BlackPawn"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("21")
					self.ChessCells[i][j].grid(row=i,column=j)

				elif(i==6):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["WhitePawn"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("11")
					self.ChessCells[i][j].grid(row=i,column=j)					

				elif((i==7 and j==0) or (i==7 and j==7)):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["WhiteRook"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("12")
					self.ChessCells[i][j].grid(row=i,column=j)

				elif((i==7 and j==1) or (i==7 and j==6)):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["WhiteKnight"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("14")
					self.ChessCells[i][j].grid(row=i,column=j)

				elif((i==7 and j==2) or (i==7 and j==5)):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["WhiteBishop"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("13")
					self.ChessCells[i][j].grid(row=i,column=j)

				elif(i==7 and j==3):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["WhiteKing"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("16")
					self.ChessCells[i][j].grid(row=i,column=j)

				elif(i==7 and j==4):
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["WhiteQueen"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("15")
					self.ChessCells[i][j].grid(row=i,column=j)

				else:
					self.ChessCells[i].append(Button(self.ChessGridFrame,image=globals.ImageDict["Transparent"],command = lambda i=i,j=j : self.CellSelect(i,j)))
					globals.ChessGrid[i].append("0")
					self.ChessCells[i][j].grid(row=i,column=j)					
					

		#chess grid background 1-gray/black 0-white
		a = "10101010"
		b = "01010101"
		for i in range(0,8):
			for j in range(0,8):
				if(i%2 == 0):
					seq = b
				else:
					seq = a
				if(seq[j] == '1'):
					self.ChessCells[i][j].configure(background="gray")
				else:
					self.ChessCells[i][j].configure(background="white")


	#check if selected cell has a valid piece in it according to player and store row and column indices
	def CellSelect(self,row,column):
		
		if(globals.TURN == 1 and globals.ChessGrid[row][column][0] == '1' and globals.ChessGrid[row][column] in globals.ChessPieces):
			globals.PieceSelected = True
			globals.PieceSelectedRow = row
			globals.PieceSelectedColumn = column
		elif(globals.TURN == 2 and globals.ChessGrid[row][column][0] == '2' and globals.ChessGrid[row][column] in globals.ChessPieces):
			globals.PieceSelected = True
			globals.PieceSelectedRow = row
			globals.PieceSelectedColumn = column
		elif(globals.PieceSelected): #move to selected cell if a piece to move has already been selected in previous click
			self.MovePiece(row,column,globals.PieceSelectedRow,globals.PieceSelectedColumn,globals.ChessGrid[globals.PieceSelectedRow][globals.PieceSelectedColumn])


	#confirm valid move and move piece from (PieceSelectedRow,PieceSelectedColumn) -> (toRow,toColumn)
	def MovePiece(self,toRow,toColumn,fromRow,fromCol,Piece):

		print("move "+Piece+" from "+str(globals.PieceSelectedRow)+","+str(globals.PieceSelectedColumn)+" to "+str(toRow)+","+str(toColumn))
		
		#if move is valid create new image at new location
		if(validmove.validMove(globals.PieceSelectedRow,globals.PieceSelectedColumn,toRow,toColumn,Piece)):
			self.CreateImage(toRow,toColumn,globals.PieceSelectedRow,globals.PieceSelectedColumn,Piece)
		else:
			print("invalid move")
			return

		#change turn of player 1 to 2 or to AI 
		if(globals.TURN == 1):
			
			if(globals.AI_on):
				moves = [] #stores available moves for a piece
				heuristic = 0 #stores heuristic of chosen move
				makeMove = [0,0,0,0] #[fromRow,fromCol,toRow,toCol]
				noMove = True #reason to use forgotten need time to remember

				for i in range(0,8):
					for j in range(0,8):

						#if piece belongs to AI ( AI pieces are black)
						if(globals.ChessGrid[i][j][0] == "2"):

							#get moves of the piece
							print("main.py - Getting moves for "+globals.ChessGrid[i][j]+' at '+str(i)+','+str(j))
							moves = ai.getAllMoves(globals.ChessGrid,i,j,globals.ChessGrid[i][j][1],globals.ChessGrid[i][j][0])
							print("moves are :")
							print(moves)
							print()

							#for every possible move
							for move in moves:

								#copy the grid status to a new list
								print("playing move "+str(move))
								NewChessGrid = deepcopy(globals.ChessGrid)

								#perform the move
								NewChessGrid[move[0]][move[1]] = globals.ChessGrid[i][j]
								NewChessGrid[i][j] = "0"

								#perform MINIMAX/ALPHA-BETA
								moveHeuristic = ai.AI_Move(NewChessGrid)
								print("back to main.py moveHeuristic = "+str(moveHeuristic) + " checking "+globals.ChessGrid[i][j])

								#set the static variable controlling depth of recursion of minimax to 0
								ai.AI_Move.depth = 0

								#if heuristic is same as previous then chose generated move by a chance
								if(moveHeuristic == heuristic):
									randomInt = randint(1,100)
									if(randomInt > 50):
										moveHeuristic = heuristic
										makeMove = [i,j,move[0],move[1]]

								#if better heuristic from move choose this move
								if(moveHeuristic < heuristic or (move == [0,0,0,0])):
									moveHeuristic = heuristic
									makeMove = [i,j,move[0],move[1]]
								if(noMove):
									moveHeuristic = heuristic
									makeMove = [i,j,move[0],move[1]]
									noMove = False

				globals.ChessGrid[makeMove[2]][makeMove[3]] = globals.ChessGrid[makeMove[0]][makeMove[1]]
				globals.ChessGrid[makeMove[0]][makeMove[1]] = "0"
				#globals.PrintGrid(globals.ChessGrid)
				self.CreateImage(makeMove[2],makeMove[3],makeMove[0],makeMove[1],globals.ChessGrid[makeMove[2]][makeMove[3]])				

			else:
				globals.TURN = 2
		else:
			globals.TURN = 1

		PieceSelected = False

	def CreateImage(self,toRow,toColumn,fromRow,fromColumn,Piece):
		print('=================================================')
		print("moving "+str(Piece)+" from "+str(fromRow)+','+str(fromColumn)+" to "+str(toRow)+','+str(toColumn))
		print('=================================================')

		#create image at new location
		if(Piece == "11"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["WhitePawn"])
		elif(Piece == "12"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["WhiteRook"])
		elif(Piece == "13"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["WhiteBishop"])
		elif(Piece == "14"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["WhiteKnight"])
		elif(Piece == "15"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["WhiteQueen"])
		elif(Piece == "16"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["WhiteKing"])
		elif(Piece == "21"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["BlackPawn"])
		elif(Piece == "22"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["BlackRook"])
		elif(Piece == "23"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["BlackBishop"])
		elif(Piece == "24"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["BlackKnight"])
		elif(Piece == "25"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["BlackQueen"])
		elif(Piece == "26"):
			self.ChessCells[toRow][toColumn].configure(image = globals.ImageDict["BlackKing"])
		
		#remove image at old location
		self.ChessCells[fromRow][fromColumn].configure(image=globals.ImageDict["Transparent"])	


#initialize Image dictionary objects
def InitializePictures():
	path = "img/"
	globals.ImageDict["BlackPawn"] = PhotoImage(file=path+"black-pawn.png",width="60",height="60")
	globals.ImageDict["WhitePawn"] = PhotoImage(file=path+"white-pawn.png",width="60",height="60")
	globals.ImageDict["BlackBishop"] = PhotoImage(file=path+"black-bishop.png",width="60",height="60")
	globals.ImageDict["WhiteBishop"] = PhotoImage(file=path+"white-bishop.png",width="60",height="60")
	globals.ImageDict["BlackQueen"] = PhotoImage(file=path+"black-queen.png",width="60",height="60")
	globals.ImageDict["WhiteQueen"] = PhotoImage(file=path+"white-queen.png",width="60",height="60")
	globals.ImageDict["BlackKing"] = PhotoImage(file=path+"black-king.png",width="60",height="60")
	globals.ImageDict["WhiteKing"] = PhotoImage(file=path+"white-king.png",width="60",height="60")
	globals.ImageDict["BlackRook"] = PhotoImage(file=path+"black-rook.png",width="60",height="60")
	globals.ImageDict["WhiteRook"] = PhotoImage(file=path+"white-rook.png",width="60",height="60")
	globals.ImageDict["BlackKnight"] = PhotoImage(file=path+"black-knight.png",width="60",height="60")
	globals.ImageDict["WhiteKnight"] = PhotoImage(file=path+"white-knight.png",width="60",height="60")
	globals.ImageDict["WhiteBlank"] = PhotoImage(file=path+"white-blank.png",width="60",height="60")
	globals.ImageDict["GrayBlank"] = PhotoImage(file=path+"gray-blank.png",width="60",height="60")
	globals.ImageDict["Transparent"] = PhotoImage(file=path+"transparent.png",width="60",height="60")

def main():
	
	#intialize global variables
	globals.init()

	root = Tk()
	root.geometry("600x600+200+200")

	#initialize image dictionary
	InitializePictures()

	game = MainWindow(root)
	game.master.title("Chess")
	root.mainloop()

if __name__ == "__main__":
	main()