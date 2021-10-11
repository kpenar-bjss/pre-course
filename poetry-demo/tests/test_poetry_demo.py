from poetry_demo import __version__
from unittest.mock import patch, call
import tictactoe.py


def test_version():
    assert __version__ == '0.1.0'


@patch('builtins.print')
def test_display_board(mocked_print, board_object):
    board_object.print_board()

    assert mocked_print.mock_calls == [call('----\n----\n----')]