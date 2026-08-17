from maze import CellMap, MazeGenerator
from maze import maze_config


def get_bitmask_matrix(cellmap: CellMap) -> list[list[str]]:
    return [
        [f"{cell.get_cell_bitmask():x}" for cell in row]
        for row in cellmap.grid
    ]


def write_maze(cellmap: CellMap, output_file: str) -> None:
    bitmask = get_bitmask_matrix(cellmap)

    try:
        with open(output_file, "w") as file:
            for row in bitmask:
                file.write("".join(row) + "\n")

    except OSError as e:
        raise OSError(
            f"Could not write maze to '{output_file}': {e}"
        ) from e


def main() -> None:
    config_info = maze_config.parse_to_dict("config.txt")
    config = maze_config.maze_config_from_dict(config_info)

    cellmap = CellMap(
        width=config.width,
        height=config.height,
    )

    generator = MazeGenerator(
        cellmap=cellmap,
        seed=config.seed,
    )

    generator.generate(config.perfect)

    write_maze(
        cellmap,
        config.output_file,
    )


if __name__ == "__main__":
    main()
