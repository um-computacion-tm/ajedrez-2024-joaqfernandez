from piece import Piece


class Rook(Piece):
    class Rook(Piece):
        white_str = "♜"
        black_str = "♖"
    
    def posiciones_validas(
            self, 
            from_col,
            from_row,
            to_col, 
            to_row
    ):
        posible_posiciones = (
            posibles_posiciones_vd(from_row, from_col) +
            possible_positions_va(from_row, from_col)
        )
        return (to_row, to_col) in posible_posiciones:
    
    def posibles_posiciones_vd(self, row, col):
        posibles = []
        for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    posibles.append((next_row, col))
                break
            posibles.append((next_row, col))
        return posibles
            