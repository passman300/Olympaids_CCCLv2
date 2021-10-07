def row_paint(index, canvas):
    for i in range(len(canvas[ index ])):
        canvas[ index ][ i ] = not canvas[ index ][ i ]
    return canvas


def column_paint(index, canvas):
    for i in range(len(canvas)):
        canvas[ i ][ index ] = not canvas[ i ][ index ]
    return canvas


def translateBG(canvas):
    count = 0
    for i in canvas:
        for j in i:
            if j:
                count += 1
    return count


M = int(input())  # height
N = int(input())  # width

canvas = [ [ False for i in range(N) ] for j in range(M) ]

K = int(input())
for i in range(K):
    line = input().split(" ")
    RC = line[0]
    index = int(line[ 1 ]) - 1
    if RC == "R":
        canvas = row_paint(index, canvas)
    else:
        canvas = column_paint(index, canvas)

print(translateBG(canvas))
