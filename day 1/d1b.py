from collections import defaultdict

def process(fileName):
    count = 0
    left = defaultdict(lambda: 0)
    right = defaultdict(lambda: 0)
    with open(fileName, 'r') as f:
        line = f.readline()
        while line:
            (a, b) = map(int, line.split())
            left[a] += 1
            count += right[a] * a
            right[b] += 1
            count += left[b] * b
            line = f.readline()

    print(f'{fileName}: {count}')
    return count


assert process('d1a.ex.data') == 31
process('d1a.data')        

