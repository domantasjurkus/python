# returns complete list of rows
def readData():
    file = open("18_data.txt", "r")
    list = []

    line = file.readline()
    while line != "":
        line = line[:-1]
        row = map(int, line.split())
        list.append(row)
        line = file.readline()

    return list

def getEntry(d, row, col):
    return d[row][col]

def placeEntry(d, row, col, val):
    d[row][col] = val


data = readData()

# we start with the second-last row
row = len(data)-2

while row >= 0:
    # now for each value in the penultimate row
    for i in xrange(len(data[row])):
        topValue = getEntry(data, row, i)
        bottom1 = getEntry(data, row+1, i)
        bottom2 = getEntry(data, row+1, i+1)

        if bottom1 > bottom2:
            placeEntry(data, row, i, topValue+bottom1)
        else:
            placeEntry(data, row, i, topValue+bottom2)

    row -= 1

print data[0][0]