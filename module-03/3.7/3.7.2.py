# 3.7.2 Two dimensional Arrays

board = [["EMPTY" for i in range(8)] for j in range(8)]

board[0][0] = "ROOK"
board[0][7] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"

board[4][2] = "KNIGHT"

board[3][4] = "PAWN"

print(board, end="\n")