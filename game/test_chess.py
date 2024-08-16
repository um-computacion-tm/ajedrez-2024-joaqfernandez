from chess import Chess
from board import Board
import unittest


class testChess(unittest.TestCase):

    chess = Chess()

    def test_turno_inicial(self):
        self.assertEqual(self.chess.turn, "WHITE")
    




if __name__ == '__main__':
    unittest.main()