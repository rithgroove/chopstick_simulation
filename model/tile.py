from dataclasses import dataclass

@dataclass
class Tile:
    x: int
    y: int
    elevation: int = 0
    cover: int = 0  # 0 = none, 1 = half, 2 = full