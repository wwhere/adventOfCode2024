"""Import reusable functions from part 1"""
from d8a import in_grid, read_input


def find_antinodes_for_antenna(grid, positions):
    """Find the antinodes generated by a list of antenna positions

    Args:
        grid (list): the grid
        positions (list): A list of antenna positions

    Returns:
        list: A list of antinodes positions
    """
    antinodes = []

    if len(positions) > 2:
        for p in positions:
            antinodes.append(p)

    antenna_pairs = [(p1, p2)
                     for i1, p1 in enumerate(positions)
                     for i2, p2 in enumerate(positions)
                     if i2 > i1]

    for p1, p2 in antenna_pairs:
        dist = p2-p1
        antinode = p1
        while in_grid(grid, antinode-dist):
            antinode = antinode-dist
            antinodes.append(antinode)

        antinode = p2
        while in_grid(grid, antinode+dist):
            antinode = antinode+dist
            antinodes.append(antinode)

    return antinodes


def process(filename):
    """Find the solution for a data file

    Args:
        filename (str): The data file name

    Returns:
        int: Solution for the data file
    """
    grid, antennas = read_input(filename)

    antinodes = []
    for antenna_positions in antennas.values():
        antinodes += find_antinodes_for_antenna(grid, antenna_positions)

    antinodes = list(dict.fromkeys(antinodes))

    count = len(antinodes)

    print(f'{filename}: {count}')
    return count


if __name__ == "__main__":
    assert process('d8b.ex.data') == 9
    assert process('d8a.ex.data') == 34
    assert process('d8a.data') == 1067
