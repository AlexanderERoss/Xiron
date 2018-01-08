###############################################################################
# ChessEngine v 0.0.0.1
# Created by Alexander Ross
# alexander.eric.ross@gmail.com
###############################################################################

import numpy as np
import re


class ChessEngine(object):
    def __init__(self, pgn_match):
        self.initial_state = np.matrix([['WR1', 'WN1', 'WB1', 'WQ1',
                                         'WKg', 'WB2', 'WN2', 'WR2'],
                                        ['WP1', 'WP2', 'WP3', 'WP4',
                                         'WP5', 'WP6', 'WP7', 'WP8'],
                                        [0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0],
                                        ['BP1', 'BP2', 'BP3', 'BP4',
                                         'BP5', 'BP6', 'BP7', 'BP8'],
                                        ['BR1', 'BN1', 'BB1', 'BQ1',
                                         'BKg', 'BB2', 'BN2', 'BR2']])


class pgn_list(object):
    '''Creates a list of pgn objects from a file-name'''

    def __init__(self, pgn_filename):
        self.pgns_file = open(pgn_filename)

    def pgn_gen(self):
        pgns = []
        pgn_start = True

        pgn_txt = ""
        for line in self.pgns_file:
            if re.search("^\\[", line) and pgn_start:
                pgn_start = False
                if pgn_txt != "":
                    pgns.append(pgn(pgn_txt))
                pgn_txt = line
            else:
                if not re.search("^\\[", line):
                    pgn_start = True
                pgn_txt += line
        self.pgns = pgns
        return pgns


class pgn(object):
    '''An object which contain all the information of a pgn_file but encoded,
    tabulate and accessible on a move by move basis'''

    def __init__(self, pgn_raw_text):
        self.pgn_txt = pgn_raw_text
        self.moves = moves

    def gen_dets(self):
        dets_txt = re.findall('\\[.+\\]', pgn_raw_text)
        details = {}
        for det in det_txt:
            details[re.findall('(?<=^\[)\S+',
                               det)[0]] = re.findall('(?<=\").+(?=\")', det)[0]

    def gen_moves(self):
        pass
