from .cell import Cell


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

    def remove_wall(self, first: Cell, second: Cell) -> None:
        dx = second.x_coord - first.x_coord
        dy = second.y_coord - first.y_coord

        if dx == 1:
            first.east_wall = False
            second.west_wall = False

        elif dx == -1:
            first.west_wall = False
            second.east_wall = False

        elif dy == 1:
            first.south_wall = False
            second.north_wall = False

        elif dy == -1:
            first.north_wall = False
            second.south_wall = False

        else:
            raise ValueError("Cells are not adjacent.")

    def add_wall(self, first: Cell, second: Cell) -> None:
        dx = second.x - first.x
        dy = second.y - first.y

        if dx == 1:
            first.east_wall = True
            second.west_wall = True

        elif dx == -1:
            first.west_wall = True
            second.east_wall = True

        elif dy == 1:
            first.south_wall = True
            second.north_wall = True

        elif dy == -1:
            first.north_wall = True
            second.south_wall = True

        else:
            raise ValueError("Cells are not adjacent.")
