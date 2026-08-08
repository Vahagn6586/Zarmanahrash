from pydantic import BaseModel, Field, model_validator, field_validator, ValidationError
from typing import Any


class MazeConfig(BaseModel):
    width: int = Field(gt=0, description="Width of the maze")
    height: int = Field(gt=0, description="Height of the maze")
    start: tuple[int, int] = Field(description="Starting position in the maze")
    end: tuple[int, int] = Field(description="Ending position in the maze")
    output_file: str = Field(default="maze.txt", description="Path to the output file for the maze")
    is_perfect: bool = Field(default=True, description="Whether the maze should be perfect (no loops)")
    seed: int = Field(default=42, description="Random seed for maze generation")

    @field_validator("start", "end")
    @classmethod
    def validate_coordinates(cls, value: Any, values: Any) -> Any:
        width = values.get("width")
        height = values.get("height")
        if not (0 <= value[0] < width) or not (0 <= value[1] < height):
            raise ValueError(f"Coordinates {value} are out of bounds for maze size {width}x{height}")
        return value

    @model_validator(mode="after")
    @classmethod
    def validate_maze_config(cls, values: Any) -> Any:
        start = values.get("start")
        end = values.get("end")

        if start == end:
            raise ValueError("Start and end positions cannot be the same.")
        
        return values


def parse_to_dict(filepath: str) -> dict[str, str]:
    """
    Parses a configuration file and returns a dictionary of the configuration.

    Args:
        filepath (str): Path to the configuration file.

    Returns:
        dict[str, str]: Dictionary containing the configuration parameters.
    """
    config_dict = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):  # Ignore empty lines and comments
                    key, value = line.split("=", 1)
                    config_dict[key.strip()] = value.strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{filepath}' not found.")
    except Exception as e:
        raise ValueError(f"Error parsing configuration file: {e}")

    return config_dict

def maze_config_from_dict(config_dict: dict[str, str]) -> MazeConfig:
    """
    Creates a MazeConfig object from a dictionary of configuration parameters.

    Args:
        config_dict (dict[str, str]): Dictionary containing the configuration parameters.

    Returns:
        MazeConfig: A MazeConfig object initialized with the configuration parameters.
    """
    try:
        return MazeConfig(**config_dict)
    except ValidationError as e:
        raise ValueError(f"Invalid configuration parameters: {e}") from e