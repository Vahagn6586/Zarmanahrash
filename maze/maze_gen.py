from cellmap import CellMap, Cell
import random


class MazeGenerator:
    cellmap: CellMap
    pattern_set: set[tuple[int, int]] = {
            (-3, 2),
            (-3, 1),
            (-3, 0),
            (-2, 0),
            (-1, 0),
            (-1, -1),
            (-1, -2),
            (1, 2),
            (2, 2),
            (3, 2),
            (3, 1),
            (3, 0),
            (2, 0),
            (1, 0),
            (1, -1),
            (1, -2),
            (2, -2),
            (3, -2)
        }

    def __init__(self, cellmap: CellMap, seed: int) -> None:
        self.cellmap = cellmap
        self.random = random.Random(seed)

    def generate(self) -> None:
        start = self.cellmap.grid[0][0]
        self.prim_gen(start)

    def pattern_gen(self) -> set[tuple[int, int]]:
        offset_x = self.cellmap.width // 2
        offset_y = self.cellmap.height // 2
        return {
            (x + offset_x, y + offset_y)
            for x, y in self.pattern_set
        }

    def is_blocked(self, cell: Cell) -> bool:
        return (cell.x_coord, cell.y_coord) in self.pattern_set

    def prim_gen(self, cell: Cell):
        cell.visited = True

        frontier = [
            neighbor
            for neighbor in self.cellmap.get_neighbors(cell)
            if not self.is_blocked(neighbor)
        ]

        while frontier:
            cell = self.random.choice(frontier)
            frontier.remove(cell)

            visited_neighbors = [
                neighbor
                for neighbor in self.cellmap.get_neighbors(cell)
                if neighbor.visited and not self.is_blocked(neighbor)
            ]

            neighbor = self.random.choice(visited_neighbors)

            self.cellmap.remove_wall(cell, neighbor)

            cell.visited = True

            for neighbor in self.cellmap.get_neighbors(cell):
                if (
                    not neighbor.visited
                    and not self.is_blocked(neighbor)
                    and neighbor not in frontier
                ):
                    frontier.append(neighbor)

    def validate_prim(self) -> bool:
        for row in self.cellmap.grid:
            for cell in row:
                if not (cell.visited) and not self.is_blocked(cell):
                    return False
        return True
