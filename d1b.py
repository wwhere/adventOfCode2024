"""modules"""
from collections import defaultdict
from aocTools import getLines


def process(filename):
    """Daily processing

    Args:
        fileName (str): Name of the data file to process

    Returns:
        int: Value for that file
    """
    count = 0
    left = defaultdict(lambda: 0)
    right = defaultdict(lambda: 0)
    for line in getLines(filename):
        (a, b) = map(int, line.split())
        left[a] += 1
        count += right[a] * a
        right[b] += 1
        count += left[b] * b

    print(f'{filename}: {count}')
    return count


assert process('d1a.ex.data') == 31
process('d1a.data')
