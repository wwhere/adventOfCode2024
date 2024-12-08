from aocTools import getLines

dayData = "8a"

empty = '.'


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, o):
        return Vector2(self.x - o.x, self.y - o.y)

    def __add__(self, o):
        return Vector2(self.x + o.x, self.y + o.y)

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __hash__(self):
        return hash((self.x, self.y))


def readInput(fileName):
    antennas = {}
    grid = []
    for line in getLines(fileName):
        gridLine = []
        for c in line:
            if c != empty:
                antennas[c] = antennas.get(c, []) + [Vector2(len(grid), len(gridLine))]
            gridLine.append(c)
        grid.append(gridLine)
    return grid, antennas


def inGrid(grid, position: Vector2):
    return not (position.x < 0 or position.x >= len(grid) or position.y < 0 or position.y >= len(grid[position.x]))


def findAntinodesForAntenna(grid, positions):
    antinodes = []

    for i1 in range(len(positions)-1):
        for i2 in range(i1+1, len(positions)):
            p1: Vector2 = positions[i1]
            p2: Vector2 = positions[i2]
            dist = p2-p1
            antinode1 = p1 - dist
            antinode2 = p2 + dist
            if inGrid(grid, antinode1):
                antinodes.append(antinode1)
            if inGrid(grid, antinode2):
                antinodes.append(antinode2)

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
    assert process(f'd{dayData}.ex.data') == 14
    process(f'd{dayData}.data')
