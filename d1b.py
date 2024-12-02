from collections import defaultdict
from aocTools import getLines


def process(fileName):
    count = 0
    left = defaultdict(lambda: 0)
    right = defaultdict(lambda: 0)
    for line in getLines(fileName):
        (a, b) = map(int, line.split())
        left[a] += 1
        count += right[a] * a
        right[b] += 1
        count += left[b] * b

    print(f'{fileName}: {count}')
    return count


assert process('d1a.ex.data') == 31
process('d1a.data')
