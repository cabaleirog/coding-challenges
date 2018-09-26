"""Ways to give a check.

https://www.hackerrank.com/contests/w36/challenges/ways-to-give-a-check/

- Difficulty: Medium

Chess is a game played worldwide and chess engines such as Stockfish and Komodo
help us analyze chess games. In this problem, the task is to implement a very
simple pawn promotion component that can be used in a chess engine.

For clarity, White promotes the Pawn by moving it from the 7th to the 8th
rank (row) along the same file (column). There are 4 possible different
promotions: the pawn can be promoted either to a Queen, or to a Rook, or to a
Bishop, or to a Knight.

- You should assume that there is no position on the board in which the Pawn
can be moved to the 8th rank by capturing the Black's piece (A diagonal move).

- Moves resulting in a checkmate also count.

Moreover, White can have more than one Pawn in the 7th rank, but there will be
exactly one that can be promoted with a single valid move. In other words,
there might be more White's Pawns in the 7th rank, but only one can make a
valid move along its file to the 8th rank. Your task is to find the number of
ways to promote the white pawn in the 7th rank, to the right piece (Queen,
Rook, Bishop or Knight) such that after the promotion Black's King is in check.

Complete a function that takes a 2-D char array as input, describing the
positions of various pieces on the board, and return an integer denoting the
number of ways to end up in a check scenario.

Input Format:

In the first line, there is a single integer t denoting the number of scenarios
to handle. After that, descriptions of subsequent scenarios are given.

Each scenario consists of 8 lines, with 8 characters each. The first line
denotes the 8th rank (row) on the board, while the last line denotes the 1st
rank. Empty cells on the board are denoted by "#", while pieces are denoted by
characters {K, Q, N, B, R, P} for White's pieces and {k, q, n, b, r, p} for
Black's pieces, where K/k is the King, Q/q is a Queen, N/n is a Knight, B/b is
a Bishop, R/r is a Rook, and P/p is a Pawn).

"""
import os
import string
import logging


console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(console)


class CheckPiece:
    def __init__(self):
        pass


class CheckGame:

    def __init__(self):
        self.board = None
        self.white = None
        self.black = None

    def set_board(self, board):
        if not board or len(board) != len(board[0]):
            raise ValueError('Invalid board dimensions')
        self.board = board
        self.white, self.black = self.piece_locations()
        return self.board

    @property
    def board_size(self):
        return len(self.board)

    def ways_to_give_a_check(self):
        total_ways = 0

        white, black = self.white, self.black
        king = next(filter(lambda x: x[0] == 'k', black))
        pawns = self.get_pawns(white)

        logger.info('White pieces: %s', self.white)
        logger.info('Black pieces: %s', self.black)
        logger.info('Pawns: %s', pawns)

        for pawn in pawns:
            if not self.is_pawn_promotable(pawn, white + black):
                continue

            # FIXME: updated_board is not actually a board, only the pieces.
            updated_board = self.remove_from_board(pawn, white + black)
            pawn[1] = 0  # move pawn to row 0 (8th rank).

            for new_piece in self.get_promoted_pieces(pawn):
                if self.is_check(new_piece, king, updated_board):
                    logger.info('King on check by %s', new_piece)
                    total_ways += 1

            # verify if the king is in check by another white piece.
            other_pieces = self.remove_from_board(pawn, white)
            for piece in other_pieces:
                if self.is_check(piece, king, updated_board):
                    # discovered attack; any promotion causes a check.
                    logger.info('Discovered check by %s', piece)
                    total_ways = 4
                    break  # already in check by one white piece.

        return total_ways

    def get_promoted_pieces(self, pawn):
        return [[x, pawn[1], pawn[2]] for x in ('Q', 'N', 'B', 'R')]

    def get_pawns(self, pieces):
        return [x for x in pieces if x[0] == 'P']

    def remove_from_board(self, piece, pieces):
        new_board = pieces[:]
        new_board.remove(piece)
        return new_board

    def is_pawn_promotable(self, pawn, pieces):
        _, row, col = pawn
        piece_ex_pawn = [x[1:] for x in self.remove_from_board(pawn, pieces)]

        # exclude any pawn which is not in the 7th rank.
        if row != 1:
            return False

        # exclude if the square is already occupied.
        if (0, col) in piece_ex_pawn:
            return False

        # verify if moving the pawn causes a check on its own king.
        blacks = [x for x in self.black if x[0] != 'k']
        white_king = next(filter(lambda x: x[0] == 'K', self.white))
        for black in blacks:
            if self.is_check(black, white_king, piece_ex_pawn):
                return False  # invalid move, check on its own king.

        logger.info('Pawn %s can be promoted.', pawn)
        return True

    def is_check(self, piece, king, board):
        logger.debug('Checking to see if %s can check king %s', piece, king)

        king_pos = tuple(king[1:])
        attacker = piece[0].upper()

        if attacker == 'N':
            return king_pos in self.knight_movement(*piece[1:])[0]

        if attacker == 'R' or attacker == 'Q':
            movements = self.rook_movement(*piece[1:])
            for movement in movements:
                logger.debug('Checking %s by moving %s', attacker, movement)
                for position in movement:
                    if position == king_pos:
                        return True
                    if self.is_blocked(position, board):
                        break

        if attacker == 'B' or attacker == 'Q':
            movements = self.bishop_movement(*piece[1:])
            for movement in movements:
                for position in movement:
                    if position == king_pos:
                        return True
                    if self.is_blocked(position, board):
                        break
        return False

    def piece_locations(self):
        white = []
        black = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                character = self.board[i][j]
                if character in string.ascii_lowercase:
                    black.append([character, i, j])
                elif character in string.ascii_uppercase:
                    white.append([character, i, j])
        return white, black

    def is_blocked(self, position, pieces):
        # FIXME: quick hack to fix issue with tuples and lists.
        position = list(position)

        # sanity check
        if pieces and len(pieces[0]) != 2:
            return position in [x[1:] for x in pieces]
        return position in pieces

    def knight_movement(self, row, col):
        moves = [
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row - 2, col + 1),
            (row - 2, col - 1),
            (row + 1, col - 2),
            (row - 1, col - 2),
            (row + 1, col + 2),
            (row - 1, col + 2)]
        return self._inside_board([moves])

    def bishop_movement(self, row, col):
        # order: right-down, right-up, left-down, left-up.
        moves = [
            [(row + x, col + x) for x in range(1, 8)],
            [(row - x, col + x) for x in range(1, 8)],
            [(row + x, col - x) for x in range(1, 8)],
            [(row - x, col - x) for x in range(1, 8)]]
        return self._inside_board(moves)

    def rook_movement(self, row, col):
        moves = [
            [(row, col + x) for x in range(1, 8 - col)],
            [(row, col - x) for x in range(1, 1 + col)],
            [(row + x, col) for x in range(1, 8 - row)],
            [(row - x, col) for x in range(1, 1 + row)]]
        return self._inside_board(moves)

    def queen_movement(self, row, col):
        return self.rook_movement(row, col) + self.bishop_movement(row, col)

    def _inside_board(self, mvl):
        """Remove moves outside of the board."""
        n = self.board_size
        return [[x for x in y if 0 <= x[0] < n and 0 <= x[1] < n] for y in mvl]


def read_input(filename=None):
    if filename:
        path = os.path.join(os.path.dirname(__file__), filename)
        with open(path) as f:
            for _ in range(int(f.readline().strip())):
                yield [list(f.readline().strip()) for _ in range(8)]
    else:
        for _ in range(int(input().strip())):
            yield [list(input().strip()) for _ in range(8)]


if __name__ == '__main__':
    for board in read_input('test-cases/ways-to-give-a-check-input0.txt'):
        game = CheckGame()
        game.set_board(board)
        total_ways = game.ways_to_give_a_check()
        print(total_ways)
