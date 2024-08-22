import unittest
from unittest.mock import patch
from chess import Chess
from cli import play

class TestCli(unittest.TestCase):
    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    )