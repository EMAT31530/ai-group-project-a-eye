
import chess
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, HTML, clear_output

board = chess.Board()

#print(board)
#print(board.legal_moves)
#print(board.piece_at(chess.C1))

print(chess.svg.piece(chess.Piece.from_symbol("R")))