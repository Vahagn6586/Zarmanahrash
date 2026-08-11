# import maze_config
from cell import Cell


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

    def remove_wall(self, first: Cell, second: Cell) -> None:
        dx = second.x - first.x
        dy = second.y - first.y

        if dx == 1:
            first.east = False
            second.west = False

        elif dx == -1:
            first.west = False
            second.east = False

        elif dy == 1:
            first.south = False
            second.north = False

        elif dy == -1:
            first.north = False
            second.south = False

        else:
            raise ValueError("Cells are not adjacent.")

    def add_wall(self, first: Cell, second: Cell) -> None:
        dx = second.x - first.x
        dy = second.y - first.y

        if dx == 1:
            first.east = True
            second.west = True

        elif dx == -1:
            first.west = True
            second.east = True

        elif dy == 1:
            first.south = True
            second.north = True

        elif dy == -1:
            first.north = True
            second.south = True

        else:
            raise ValueError("Cells are not adjacent.")
