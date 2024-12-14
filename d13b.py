"""Advent of Code specific utilities"""
from aoc_tools import read_lines

A_COST = 3
B_COST = 1
MAX_PRESS = 100


class Claw:
    a_x = 0
    a_y = 0
    b_x = 0
    b_y = 0
    x = 0
    y = 0


def solve(c: Claw):

    a = (c.b_y * c.x - c.b_x * c.y) / (c.a_x*c.b_y - c.a_y*c.b_x)
    b = (c.y * c.a_x - c.x * c.a_y) / (c.a_x * c.b_y - c.a_y * c.b_x)

    if a.is_integer() and b.is_integer():
        return int(a*A_COST + b*B_COST)
    else:
        return 0


def solve_all(claws: list[Claw]):
    total = 0

    for claw in claws:
        total += solve(claw)

    return total


def process(filename: str, extra=0) -> int:
    """Reads and finds the solution for the specified data file

    Args:
        fileName (str): The name of the data file

    Returns:
        int: The solution for the data file
    """
    solution = 0
    claws = []
    current_claw: Claw
    for line in read_lines(filename):
        if 'Button A' in line:
            current_claw = Claw()
            # Button A: X+94, Y+34
            current_claw.a_x, current_claw.a_y = map(int, line.replace(
                'Button A: X+', '').replace(', Y+', ',').split(','))
            continue
        if 'Button B' in line:
            # Button B: X+94, Y+34
            current_claw.b_x, current_claw.b_y = map(int, line.replace(
                'Button B: X+', '').replace(', Y+', ',').split(','))
            continue
        if 'Prize:' in line:
            # Prize: X=8400, Y=5400
            current_claw.x, current_claw.y = map(int, line.replace(
                'Prize: X=', '').replace(', Y=', ',').split(','))
            current_claw.x += extra
            current_claw.y += extra
            claws.append(current_claw)

    solution = solve_all(claws)

    print(f'{filename}: {solution}')
    return solution


if __name__ == "__main__":
    assert process('d13.1.data') == 480
    process('d13.2.data', 10000000000000)