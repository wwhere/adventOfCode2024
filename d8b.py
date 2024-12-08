from d8a import Vector2, inGrid, readInput


def findAntinodesForAntenna(grid, positions):
    antinodes = []

    if len(positions) > 2:
        for p in positions:
            antinodes.append(p)

    for i1 in range(len(positions)-1):
        for i2 in range(i1+1, len(positions)):
            p1: Vector2 = positions[i1]
            p2: Vector2 = positions[i2]
            dist = p2-p1
            antinode = p1
            while inGrid(grid, antinode-dist):
                antinode = antinode-dist
                antinodes.append(antinode)

            antinode = p2
            while inGrid(grid, antinode+dist):
                antinode = antinode+dist
                antinodes.append(antinode)

    return antinodes


def process(fileName):
    grid, antennas = readInput(fileName)

    antinodes = []
    for antenna in antennas.keys():
        antinodes = antinodes + findAntinodesForAntenna(grid, antennas[antenna])

    antinodes = list(dict.fromkeys(antinodes))

    count = len(antinodes)

    print(f'{fileName}: {count}')
    return count


if __name__ == "__main__":
    assert process(f'd8b.ex.data') == 9
    assert process(f'd8a.ex.data') == 34
    process(f'd8a.data')
