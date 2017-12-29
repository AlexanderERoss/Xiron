###############################################################################
# Chess board infograph drawing program
# Made by Alexander Ross
# Licenced under LGPL 3.0
# alexander.eric.ross@gmail.com
###############################################################################

# Dependencies
import svgwrite
# import numpy as np


class drawBoard(object):
    '''Takes the number grid from the init and prints an svg
    chessboard to the given filepath. More features to come in'''

    def __init__(self, number_board, file_path, ranger='minmax'):
        self.nb = number_board
        self.fp = file_path
        if ranger == 'minmax':
            range_max = max(max(number_board))
            self.range_min = min(min(number_board))
            self.range_val = range_max - self.range_min

    def draw_board(self):
        ch_board = svgwrite.Drawing(self.fp)
        for col in [0, 1, 2, 3, 4, 5, 6, 7]:
            for rank in [0, 1, 2, 3, 4, 5, 6, 7]:
                spect1 = (self.nb[col][rank] - self.range_min)/self.range_val
                ch_board.add(
                    ch_board.rect((rank*10, col*10),
                                  (10, 10),
                                  fill=svgwrite.rgb(
                                      r=255*spect1,
                                      g=0, b=0,
                                      mode='RGB')))

        ch_board.save()

# Prescripting

board_val = [[5, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 8],
             [1, 2, 3, 5, 5, 6, 7, 8],
             [1, 2, 3, 5, 5, 6, 7, 8],
             [1, 2, 3, 4, 5, 6, 7, 1],
             [1, 2, 3, 4, 5, 6, 7, 8]]

a = drawBoard(board_val, '/home/senex/Programs/Xiron/test.svg')
a.draw_board()
# Scripting End
