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

    def test_move_funciona(self): #move funciona correctamente
        chess = Chess()
        #simulacion que se llama la funcion move
        from_row, from_col = 0, 1 
        to_row, to_col = 0, 2
        #cuando se ejecuta move, se fija que no haya errores
        try:
            chess.move(from_row, from_col, to_row, to_col) #se verifica que haya 4 parametros
            llamado_move = True
        except Exception as e: #si no pasa eso, falso
            llamado_move = False
            print(f"Error al llamar a move: {e}")
        self.assertTrue(llamado_move)
        self.assertEqual(chess.turn, "BLACK")

if __name__ == '__main__':
    unittest.main()