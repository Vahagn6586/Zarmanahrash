*This project has been created as part of the 42 curriculum by vchiling, vrafyan.*

# A-Maze-ing

## Description

A-Maze-ing is a procedural maze generator and solver written in Python. The program reads a configuration file, generates a random maze using the **Recursive Backtracker**<!--esi pti poxvi--> algorithm, finds the shortest path from entry to exit using **BFS**<!--mec havanakanutyamb es el-->, and displays the result in the terminal with an interactive menu. The maze always contains a hidden **"42"** pattern drawn from fully closed cells.

The generation logic is packaged as a reusable pip-installable module (`mazegen-amazeing`).

---

## Instructions

### Requirements

- Python 3.10 or later
- pip

### Installation

```bash
make install
```

### Running

```bash
make run
# or directly:
python3 a_maze_ing.py config.txt
```

### Debug mode

```bash
make debug
```

### Lint

```bash
make lint
make lint-strict  # optional, stricter mypy
```

### Clean

```bash
make clean
```

---

## Configuration File Format

The config file uses `KEY=VALUE` pairs, one per line. Lines starting with `#` are comments and are ignored. Empty lines are also ignored.

| Key | Description | Example |
|-----|-------------|---------|
| `WIDTH` | Maze width in cells (positive integer) | `WIDTH=20` |
| `HEIGHT` | Maze height in cells (positive integer) | `HEIGHT=20` |
| `ENTRY` | Entry coordinates `x,y` | `ENTRY=0,0` |
| `EXIT` | Exit coordinates `x,y` | `EXIT=19,14` |
| `OUTPUT_FILE` | Output filename | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | Perfect maze? (`True` or `False`) | `PERFECT=True` |
| `SEED` | Optional seed for reproducibility | `SEED=42` |

**Example config.txt:**
```
# A-Maze-ing default config
WIDTH=20
HEIGHT=20
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
```

If `SEED` is not provided, a random seed is generated automatically.

---

## Output File Format

The output file contains one hexadecimal character per cell, where each hex digit encodes which walls are closed (bit 0 = North, bit 1 = East, bit 2 = South, bit 3 = West). Cells are stored row by row. After an empty line, the entry coordinates, exit coordinates, and shortest path (as a string of `N`, `E`, `S`, `W` letters) are written.