import svgwrite
import numpy as np


class drawBoard(object):
    '''Takes the number grid from the init and prints an svg
    chessboard to the given filepath'''

    def __init__(self, number_board, file_path):
        self.nb = number_board
        self.fp = file_path

    def draw_board(self):
        ch_board = svgwrite.Drawing(self.fp)
        for col in [0, 1, 2, 3, 4, 5, 6, 7]:
            for rank in [0, 1, 2, 3, 4, 5, 6, 7]:
                ch_board.add(
                    ch_board.rect((rank*10, col*10),
                                  (10, 10),
                                  fill=svgwrite.rgb(r=self.nb[col][rank]*30,
                                                    g=0,
                                                    b=0,
                                                    mode='RGB')))
        ch_board.save()


class ChessEngine(object):

    def __init__(self, pgn_file):
        self.initial_state = np.matrix([['WR1', 'WN1', 'WB1', 'WQ',
                                         'WK', 'WB2', 'WN2', 'WR2'],
                                        ['WP1', 'WP2', 'WP3', 'WP4',
                                         'WP5', 'WP6', 'WP7', 'WP8'],
                                        [0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0],
                                        ['BP1', 'BP2', 'BP3', 'BP4',
                                         'BP5', 'BP6', 'BP7', 'BP8'],
                                        ['BR1', 'BN1', 'BB1', 'BQ',
                                         'BK', 'BB2', 'BN2', 'BR2']])

# Prescripting

board_val = [[1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8]]

a = drawBoard(board_val, '/home/senex/Programs/Chiron/test.svg')
a.draw_board()
# Scripting End
