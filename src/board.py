from src.constants import BLACK, DIRECTIONS, GRID_SIZE, WHITE

from typing import List

class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.grid[4][4] = 1
        self.grid[5][4] = 2
        self.grid[4][5] = 2
        self.grid[5][5] = 1


        # 1 for white, 2 for black


    def get_piece(self, row: int, col: int) -> int:
        return self.grid[row][col]



    def isValidMove(self, row: int, col: int, player: int) -> bool:

        opponent = 1 if player == 0 else 1

        if self.grid[row][col] != 0:
            return False


        if row >= 8 or row < 0 or col >= 8 or col < 0:
            return False


        for dx, dy in DIRECTIONS:
            x = row + dx
            y = col + dy

            has_opp_piece = False

            while 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                if self.get_piece(x, y) == opponent:
                    has_opp_piece = True
                elif self.get_piece(x, y) == player:
                    if has_opp_piece:
                        return True # we have opp piece and our own piece in the same line
                    break

                else: # empty square, dont need to keep checking this direction
                    break

                x += dx
                y += dy


        return False


    # def place_piece(self, row, col , player):
    #
    #     if not self.isValidMove(row, col, player):
    #         return 
    #
    #
    #     else:
    #
    #         self.grid[row][col] = player # place piece
    #
    #         for 
    #
    #
    # def find_flips(self, row, col, player):
    #     for dx, dy in DIRECTIONS:
    #         x = row + dx
    #         y = col + dy
    #
    #         while 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
    #             break
    #
    #
    # def flip_pieces(self, player, pieces: List[tuple[int, int]]) -> bool:
    #
    #
    #     for x, y in pieces:
    #         self.grid[x][y] = player
    #
    #     return True






        





