"""Advent of Code specific utilities"""
from aocTools import getLines

DAY_DATA = '2a'


def process(filename: str) -> int:
    """Reads and finds the solution for the specified data file

    Args:
        fileName (str): The name of the data file

    Returns:
        int: The solution for the data file
    """
    solution = 0
    for line in getLines(filename):
        continue

    print(f'{filename}: {solution}')
    return solution


assert process(f'd{DAY_DATA}.ex.data') == 31
process(f'd{DAY_DATA}.data')
