from aocTools import getLines


def process(fileName):
    count = 0
    listA = []
    listB = []

    for line in getLines(fileName):
        a, b = map(int, line.split())
        listA.append(a)
        listB.append(b)

    listA.sort()
    listB.sort()

    for a, b in zip(listA, listB):
        count += abs(a-b)

    print(f'{fileName}: {count}')
    return count


assert process('d1a.ex.data') == 11
process('d1a.data')
