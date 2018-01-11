###############################################################################
# ChessEngine v 0.0.0.1
# Created by Alexander Ross
# alexander.eric.ross@gmail.com
###############################################################################

import numpy as np
import re


class ChessEngine(object):
    def __init__(self, pgn_match):
        self.initial_state = {'a':{'1':'WR1', '2':'WP1','3':'','4':'',
                                   '5':'', '6':'', '7':'BP8', '8':'BR2'},
                              'b':{'1':'WN1', '2':'WP2','3':'','4':'',
                                   '5':'', '6':'', '7':'BP7', '8':'BN2'},
                              'c':{'1':'WB1', '2':'WP3','3':'','4':'',
                                   '5':'', '6':'', '7':'BP6', '8':'BB2'},
                              'd':{'1':'WQ1', '2':'WP4','3':'','4':'',
                                   '5':'', '6':'', '7':'BP5', '8':'BQ1'},
                              'e':{'1':'WK', '2':'WP5','3':'','4':'',
                                   '5':'', '6':'', '7':'BP4', '8':'BK'},
                              'f':{'1':'WB2', '2':'WP6','3':'','4':'',
                                   '5':'', '6':'', '7':'BP3', '8':'BB2'},
                              'g':{'1':'WN2', '2':'WP7','3':'','4':'',
                                   '5':'', '6':'', '7':'BP2', '8':'BN1'},
                              'h':{'1':'WR2', '2':'WP8','3':'','4':'',
                                   '5':'', '6':'', '7':'BP1', '8':'BR1'}}
        self.col_ref = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

    def state2FEN(self):
        '''This is a function that transforms this engine's state to the
        standard FEN notation'''
        pass

    def _moveset(self, piece, current_pos, colour)
        if piece == 'P':
            if colour == 'W':
                if current_pos[1] == '2':
                    return W_P(current_pos)
                else:
                    return W_Pstart(current_pos)
            if colour == 'B':
                if current_pos[1] == '7':
                    return B_P(current_pos)
                else:
                    return B_Pstart(current_pos)
        if piece == 'R':
            return R(current_pos)
        if piece == 'N':
            return N(current_pos)
        if piece == 'B':
            return B(current_pos)
        if piece == 'Q':
            return Q(current_pos)
        if piece == 'K':
            return K(current_pos)
        def _diags(current_pos, num):
            pass
        def _straights(current_pos, num):
            pass
        def _L(current_pos, num = 1):
            pass

        def W_P(current_pos):
            pass

        def W_Pstart(current_pos):
            pass

        def B_P(current_pos):
            pass

        def B_Pstart(current_pos):
            pass

        def R(current_pos):
            move_set = []
            for col in 1:8:
                while True: #include boudnary andpiece bound
                    #return sets

            for rank in 1:8:
                while True: #include boundary and piece bounds
                    #return sets


class pgn_list(object):
    '''Creates a list of pgn objects from a file-name'''

    def __init__(self, pgns_filename):
        self.pgns_filename = pgns_filename
        self._pgn_gen()

    def _pgn_gen(self):
        pgns = []
        pgn_start = True
        pgns_file = open(self.pgns_filename)
        pgn_txt = ""
        for line in pgns_file:
            if re.search("^\\[", line) and pgn_start:
                pgn_start = False
                if pgn_txt != "":
                    pgns.append(pgn(pgn_txt))
                pgn_txt = line
            else:
                if not re.search("^\\[", line):
                    pgn_start = True
                pgn_txt += line
        pgns_file.close()
        self.pgns = pgns
        return pgns


class pgn(object):
    '''An object which contain all the information of a pgn_file but encoded,
    tabulate and accessible on a move by move basis'''

    def __init__(self, pgn_raw_text):
        self.pgn_txt = pgn_raw_text
        self._gen_dets()
        self._gen_moves()

    def _gen_dets(self):
        dets_txt = re.findall('\[.+\]', self.pgn_txt)
        details = {}
        for det in dets_txt:
            details[re.findall('(?<=^\[)\S+',
                               det)[0]] = re.findall('(?<=\").+(?=\")', det)[0]
        self.details = details

    def _gen_moves(self):
        mv_txt = re.sub('\[.+\]', '', self.pgn_txt)
        mv_txt = re.sub('\n', '', mv_txt)
        self.mv_txt = re.sub('\d+-\d+$', '', mv_txt)
        self.moves = re.findall('O-O-O|O-O|' + 
                                '[KQBNRP]?[a-h]?[1-8]?x?[a-h][1-8]' +
                                '=?[QBNR]?[+#]?',
                                self.mv_txt)
        return self.moves
