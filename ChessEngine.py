###############################################################################
# ChessEngine v 0.0.0.1
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


class pgn_list(object):
    '''Creates a list of pgn objects from a file-name'''

    def __init__(self, pgn_filename):
        self.pgn_file = open(pgn_filename)

    def pgn_gen(self):
        pgns = []
        pgn_start = False
        pgn_txt = ""
        for line in self.pgns_file:
            if re.search("^\\[", line) and not pgn_start:
                pgn_start = True
                if pgn_txt != "":
                    pgns.append(pgn(pgn_txt))
                pgn_txt = line
            else:
                pgn_start = False
                pgn_txt += line
        self.pgns = pgns
        return pgns


class pgn(object):
    '''An object which contain all the information of a pgn_file but encoded,
    tabulate and accessible on a move by move basis'''

    def __init__(self, pgn_raw_text):
        self.pgn_txt = pgn_raw_text
        for line in self.pgn_txt:
            moves = []
            moves.append(re.split('\d*[\.,\.\.\.]', line))

    def gen_dets(self):
        pass

    def gen_moves(self):
        pass
