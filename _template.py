"""Advent of Code specific utilities"""
from aoc_tools import read_lines


def process(filename: str) -> int:
    """Reads and finds the solution for the specified data file

    Args:
        fileName (str): The name of the data file

    Returns:
        int: The solution for the data file
    """
    solution = 0
    for line in read_lines(filename):
        continue

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('dXX.1.data') == 0
    process('dXX.2.data')
