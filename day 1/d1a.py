def process(fileName):
    count = 0
    listA = []
    listB = []
    with open(fileName, 'r') as f:
        line = f.readline()
        while line:
            a, b = map(int, line.split())
            listA.append(a)
            listB.append(b)
            line = f.readline()

    listA.sort()
    listB.sort()

    for a, b in zip(listA, listB):
        count += abs(a-b)

    print(f'{fileName}: {count}')
    return count


assert process('d1a.ex.data') == 11    
process('d1a.data')        

