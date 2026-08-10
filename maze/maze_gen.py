from cellmap import CellMap, Cell
import random


class MazeGenerator:
    cellmap: CellMap

    def __init__(self, cellmap: CellMap, seed: int) -> None:
        self.cellmap = cellmap
        self.random = random.Random(seed)

    def generate(self) -> None:
        start = self.cellmap.grid[0][0]
        self._visit(start)

    def _visit(self, cell: Cell):
        cell.visited = True

        while True:
            neighbors = self.unvisited_neighbors(cell)
            if not neighbors:
                break
            neighbor = self.random.choice(neighbors)
            self.maze.remove_wall(cell, neighbor)
            self._visit(neighbor)

    def unvisited_neighbors(self, cell):
        return [
            neighbor
            for neighbor in self.maze.neighbors(cell)
            if not neighbor.visited
        ]

    def validate_dfs(self) -> bool:
        for row in self.maze.grid:
            for cell in row:
                if not (cell.visited):
                    return False
        return True
