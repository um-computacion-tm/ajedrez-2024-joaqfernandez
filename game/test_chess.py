from chess import Chess
from board import Board
import unittest


class testChess(unittest.TestCase):

    chess = Chess()

    def test_turno_inicial(self):
        self.assertEqual(self.chess.turn, "WHITE")
    
    def test_cambio_turno(self):
        self.chess.move(0, 0, 1, 2)
        self.assertEqual(self.chess.turn, "BLACK")
        self.chess.move(0, 2, 0, 3)
        self.assertEqual(self.chess.turn, "WHITE")




if __name__ == '__main__':
    unittest.main()