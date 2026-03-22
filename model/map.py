from models.tile import Tile
import random

class Map:

    def __init__(self, size: int):
        self.size = size
        self.tiles = {}

        for x in range(size):
            for y in range(size):
                self.tiles[(x, y)] = Tile(
                    x, y,
                    elevation=random.choice([0, 1]),
                    cover=random.choice([0, 1])
                )

    def get_tile(self, x, y) -> Tile:
        return self.tiles.get((x, y))

    def in_bounds(self, x, y) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size