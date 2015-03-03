
from Tkinter import *

root = None
ImageDict = None
ChessGrid = None
ChessPieces = None
PieceSelected = None
PieceSelectedRow = None
PieceSelectedColumn = None
TURN = None
AI_on = None
MAX_DEPTH = None #max minimax depth
KingChecked = None
#ChessGrid values
# 1_ - white , 2_ - black
# _1 - pawn , _2 - rook , _3 - bishop , _4 - knight , _5 - queen , _6 - king
# 0 - empty
# 12 => white rook
# 21 => black pawn

def init():
	global root,ImageDict,ChessGrid,ChessPieces,PieceSelected
	global PieceSelectedRow,PieceSelectedColumn,TURN,AI_on
	global MAX_DEPTH
	AI_on = True
	root = None
	ImageDict = {}
	ChessGrid = []
	ChessPieces = ['11','12','13','14','15','16','21','22','23','24','25','26']
	PieceSelected = False
	PieceSelectedRow = -1
	PieceSelectedColumn = -1
	TURN = 1 # 1 - white , 2 - black
	MAX_DEPTH = 3


def PrintGrid(Grid):
	for i in range(0,8):
		print(Grid[i])
		

