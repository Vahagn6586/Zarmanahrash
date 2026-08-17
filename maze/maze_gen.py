from .cellmap import CellMap, Cell
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
    loop_rate: float = 0.1

    def __init__(self, cellmap: CellMap, seed: int = 42) -> None:
        self.cellmap = cellmap
        self.random = random.Random(seed)
        self.blocked = self.pattern_gen()

    def generate(self, is_perfect: bool = True) -> None:
        start = self.cellmap.grid[0][0]
        self.prim_gen(start)
        if not is_perfect:
            self.add_loops(self.cellmap)

    def pattern_gen(self) -> set[tuple[int, int]]:
        offset_x = self.cellmap.width // 2
        offset_y = self.cellmap.height // 2
        return {
            (x + offset_x, -y + offset_y)
            for x, y in self.pattern_set
        }

    def is_blocked(self, cell: Cell) -> bool:
        return (cell.x_coord, cell.y_coord) in self.blocked

    def prim_gen(self, cell: Cell) -> None:
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

            self.cellmap.adjust_walls(cell, neighbor, "remove")

            cell.visited = True

            for neighbor in self.cellmap.get_neighbors(cell):
                if (
                    not neighbor.visited
                    and not self.is_blocked(neighbor)
                    and neighbor not in frontier
                ):
                    frontier.append(neighbor)

    def add_loops(self, cellmap: CellMap) -> None:
        candidates = []
        amount = int(cellmap.width * cellmap.height * self.loop_rate)

        for row in self.cellmap.grid:
            for cell in row:
                if self.is_blocked(cell):
                    continue

                for neighbor in self.cellmap.get_neighbors(cell):
                    if self.is_blocked(neighbor):
                        continue

                    if (cell.x_coord, cell.y_coord) < (
                        neighbor.x_coord,
                        neighbor.y_coord,
                    ):
                        if self.cellmap.has_wall_between(cell, neighbor):
                            candidates.append((cell, neighbor))

        self.random.shuffle(candidates)

        for cell, neighbor in candidates[:amount]:
            self.cellmap.adjust_walls(cell, neighbor, "remove")

    def validate_prim(self) -> bool:
        for row in self.cellmap.grid:
            for cell in row:
                if not (cell.visited) and not self.is_blocked(cell):
                    return False
        return True
