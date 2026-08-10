from dataclasses import dataclass
from enum import IntEnum


class Walls(IntEnum):
    NORTH: 1
    EAST: 2
    SOUTH: 4
    WEST: 8


@dataclass
class Cell:

    x_coord: int = 0
    y_coord: int = 0

    north_wall: bool = True
    east_wall: bool = True
    south_wall: bool = True
    west_wall: bool = True

    visited: bool = False

    def get_cell_bitmask(self) -> int:
        mask = 0

        if self.north_wall:
            mask |= Walls.NORTH
        if self.east_wall:
            mask |= Walls.EAST
        if self.south_wall:
            mask |= Walls.SOUTH
        if self.west_wall:
            mask |= Walls.WEST

        return mask
