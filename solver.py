from maze import Cell, CellMap

class MazeSolver:
    def __init__(self, cellmap: CellMap) -> None:
        self.cellmap = cellmap

    def solve(self, start: Cell, end: Cell) -> list[Cell]:
        frontier = [start]
        visited = {(start.x, start.y)}
        parent: dict[
            tuple[int, int],
            tuple[int, int] | None
        ] = {
            (start.x, start.y): None
        }

        index = 0

        while index < len(frontier):
            cell = frontier[index]
            index += 1

            if cell == end:
                return self._reconstruct_path(parent, end)

            for neighbor in self.cellmap.get_passages(cell):
                position = (neighbor.x, neighbor.y)

                if position in visited:
                    continue

                visited.add(position)
                parent[position] = (cell.x, cell.y)
                frontier.append(neighbor)

        return []

    def _reconstruct_path(
        self,
        parent: dict[
            tuple[int, int],
            tuple[int, int] | None
        ],
        end: Cell,
    ) -> list[Cell]:

        path = []
        current = (end.x, end.y)

        while current is not None:
            x, y = current
            path.append(self.cellmap.grid[y][x])
            current = parent[current]

        path.reverse()
        return path
