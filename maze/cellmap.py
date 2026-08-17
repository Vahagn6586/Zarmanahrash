from .cell import Cell
from typing import Literal


class CellMap:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.grid = [[Cell(x, y) for x in range(width)] for y in range(height)]

    def get_cell(self, x: int, y: int) -> Cell:
        return self.grid[y][x]

    def is_boundary(self, cell: Cell) -> bool:
        return (cell.x_coord in (0, self.width - 1)
                or cell.y_coord in (0, self.height - 1))

    def get_neighbors(self, cell: Cell) -> list[Cell]:
        neighbors = []

        if cell.y_coord > 0:
            neighbors.append(self.grid[cell.y_coord - 1][cell.x_coord])

        if cell.x_coord < self.width - 1:
            neighbors.append(self.grid[cell.y_coord][cell.x_coord + 1])

        if cell.y_coord < self.height - 1:
            neighbors.append(self.grid[cell.y_coord + 1][cell.x_coord])

        if cell.x_coord > 0:
            neighbors.append(self.grid[cell.y_coord][cell.x_coord - 1])

        return neighbors

    def get_passages(self, cell: Cell) -> list[Cell]:
        passages = []

        if cell.y_coord > 0 and not cell.north_wall:
            passages.append(self.grid[cell.y_coord - 1][cell.x_coord])

        if cell.x_coord < self.width - 1 and not cell.east_wall:
            passages.append(self.grid[cell.y_coord][cell.x_coord + 1])

        if cell.y_coord < self.height - 1 and not cell.west_wall:
            passages.append(self.grid[cell.y_coord + 1][cell.x_coord])

        if cell.x_coord > 0 and not cell.south_wall:
            passages.append(self.grid[cell.y_coord][cell.x_coord - 1])

        return passages

    def adjust_walls(self, first: Cell, second: Cell,
                     mode: Literal["remove", "add"] = "remove") -> None:
        dx = second.x_coord - first.x_coord
        dy = second.y_coord - first.y_coord
        flag = False

        match mode:
            case "add":
                flag = True
            case "remove":
                flag = False

        if dx == 1:
            first.east_wall = flag
            second.west_wall = flag

        elif dx == -1:
            first.west_wall = flag
            second.east_wall = flag

        elif dy == 1:
            first.south_wall = flag
            second.north_wall = flag

        elif dy == -1:
            first.north_wall = flag
            second.south_wall = flag

        else:
            raise ValueError("Cells are not adjacent.")

    def has_wall_between(self, cell: Cell, neighbor: Cell) -> bool:
        if neighbor.x_coord == cell.x_coord + 1:
            return cell.east_wall

        if neighbor.x_coord == cell.x_coord - 1:
            return cell.west_wall

        if neighbor.y_coord == cell.y_coord + 1:
            return cell.south_wall

        if neighbor.y_coord == cell.y_coord - 1:
            return cell.north_wall

        return False
