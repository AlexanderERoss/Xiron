###############################################################################
# ChessEngine v 0.0.0.0
# Created by Alexander Ross
# alexander.eric.ross@gmail.com
###############################################################################

import numpy as np
import re


class ChessEngine(object):
    def __init__(self, pgn_match):
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


class pgns2list(object):
    def __init__(self, file_name):
        self.pgns_file = open(file_name)

    def gen_files(self):
        pgn_text_list = []
        for line in self.pgns_file:
            if :
                


class pgn2match(object):
    def __init__(self, pgn_txt):
        self.pgn_txt = pgn_txt
        for line in pgn_txt:
            moves = []
            moves.append(re.split('\d*[\.,\.\.\.]', line))

    def gen_dets(self):
        pass

    def gen_moves(self):
        pass
