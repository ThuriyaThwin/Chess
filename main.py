
from Tkinter import *
import globals
import validmove



class MainWindow(Frame):

	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent = parent
		self.init()

	def init(self):

		self.MenuBar = Frame(self.parent,background="blue")
		self.MenuBar.pack()

		self.NewGameButton = Button(self.MenuBar,text="New Game")
		self.NewGameButton.pack()

		self.BlackPiecesFrame = Frame(self.parent,background="red")
		self.BlackPiecesFrame.pack()

		# Label(self.BlackPiecesFrame,text="Black killed pieces here..").pack()
		
		self.ChessGridFrame = Frame(self.parent,background="pink")
		self.ChessGridFrame.pack()

		self.CreateGrid()

		self.WhitePiecesFrame = Frame(self.parent,background="red")
		self.WhitePiecesFrame.pack()
		
		# Label(self.WhitePiecesFrame,text="White killed pieces here..").pack()

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


	def CellSelect(self,row,column):
		
		if(globals.TURN == 1 and globals.ChessGrid[row][column][0] == '1' and globals.ChessGrid[row][column] in globals.ChessPieces):
			globals.PieceSelected = True
			globals.PieceSelectedRow = row
			globals.PieceSelectedColumn = column
		elif(globals.TURN == 2 and globals.ChessGrid[row][column][0] == '2' and globals.ChessGrid[row][column] in globals.ChessPieces):
			globals.PieceSelected = True
			globals.PieceSelectedRow = row
			globals.PieceSelectedColumn = column
		elif(globals.PieceSelected):
			self.MovePiece(row,column,globals.ChessGrid[globals.PieceSelectedRow][globals.PieceSelectedColumn])


	def MovePiece(self,toRow,toColumn,Piece):

		print("move "+Piece+" from "+str(globals.PieceSelectedRow)+","+str(globals.PieceSelectedColumn)+" to "+str(toRow)+","+str(toColumn))
		
		if(validmove.validMove(globals.PieceSelectedRow,globals.PieceSelectedColumn,toRow,toColumn,Piece)):
			
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
			
			self.ChessCells[globals.PieceSelectedRow][globals.PieceSelectedColumn].configure(image=globals.ImageDict["Transparent"])	

		else:
			print("invalid move")
			return

		if(globals.TURN == 1):
			globals.TURN = 2
		else:
			globals.TURN = 1
		PieceSelected = False


def InitializePictures():
	
	globals.ImageDict["BlackPawn"] = PhotoImage(file="img/black-pawn.png",width="60",height="60")
	globals.ImageDict["WhitePawn"] = PhotoImage(file="img/white-pawn.png",width="60",height="60")
	globals.ImageDict["BlackBishop"] = PhotoImage(file="img/black-bishop.png",width="60",height="60")
	globals.ImageDict["WhiteBishop"] = PhotoImage(file="img/white-bishop.png",width="60",height="60")
	globals.ImageDict["BlackQueen"] = PhotoImage(file="img/black-queen.png",width="60",height="60")
	globals.ImageDict["WhiteQueen"] = PhotoImage(file="img/white-queen.png",width="60",height="60")
	globals.ImageDict["BlackKing"] = PhotoImage(file="img/black-king.png",width="60",height="60")
	globals.ImageDict["WhiteKing"] = PhotoImage(file="img/white-king.png",width="60",height="60")
	globals.ImageDict["BlackRook"] = PhotoImage(file="img/black-rook.png",width="60",height="60")
	globals.ImageDict["WhiteRook"] = PhotoImage(file="img/white-rook.png",width="60",height="60")
	globals.ImageDict["BlackKnight"] = PhotoImage(file="img/black-knight.png",width="60",height="60")
	globals.ImageDict["WhiteKnight"] = PhotoImage(file="img/white-knight.png",width="60",height="60")
	globals.ImageDict["WhiteBlank"] = PhotoImage(file="img/white-blank.png",width="60",height="60")
	globals.ImageDict["GrayBlank"] = PhotoImage(file="img/gray-blank.png",width="60",height="60")
	globals.ImageDict["Transparent"] = PhotoImage(file="img/transparent.png",width="60",height="60")

def main():
	
	globals.init()

	root = Tk()
	root.geometry("600x600+200+200")
	InitializePictures()
	game = MainWindow(root)
	game.master.title("Chess")
	root.mainloop()

if __name__ == "__main__":
	main()