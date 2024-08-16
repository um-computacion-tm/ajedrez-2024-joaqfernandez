import unittest
from chess import Chess
from board import Board


class test_chess(unittest.TestCase):
    def test_turno_inicial(self):
        chess_turn = Chess()
        self.assertEqual(self.chess_turn.turn, "WHITE")
    




if __name__ == '__main__':
    unittest.main()