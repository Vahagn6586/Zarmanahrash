from maze import Cell, CellMap


class MazeSolver:
    def __init__(self, cellmap: CellMap) -> None:
        self.cellmap = cellmap

    def solve(self, start: Cell, end: Cell) -> list[Cell]:
        frontier = [start]
        visited = {(start.x_coord, start.y_coord)}
        parent: dict[
            tuple[int, int],
            tuple[int, int] | None
        ] = {
            (start.x_coord, start.y_coord): None
        }

        index = 0

        while index < len(frontier):
            cell = frontier[index]
            index += 1

            if cell == end:
                return self._reconstruct_path(parent, end)

            for neighbor in self.cellmap.get_passages(cell):
                position = (neighbor.x_coord, neighbor.y_coord)

                if position in visited:
                    continue

                visited.add(position)
                parent[position] = (cell.x_coord, cell.y_coord)
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

        path: list[Cell] = []
        current = (end.x_coord, end.y_coord)

        while current is not None:
            x, y = current
            path.append(self.cellmap.grid[y][x])
            current = parent[current]

        path.reverse()
        return path
