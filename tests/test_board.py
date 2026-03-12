from src.board import Board


def test_initializeboard():
    board = Board()


    assert board.get_piece(0, 0) == 0
    assert board.get_piece(4,4) == 1
    assert board.get_piece(4,5) == 2



