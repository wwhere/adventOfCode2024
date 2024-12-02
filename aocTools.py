def getLines(fileName):
    with open(fileName, 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()
