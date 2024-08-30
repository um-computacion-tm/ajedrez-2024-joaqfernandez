from piece import Piece


class Rook(Piece):
    class Rook(Piece):
        white_str = "♜"
        black_str = "♖"
    
    def posiciones_validas(self, from_col, from_row, to_col, to_row):