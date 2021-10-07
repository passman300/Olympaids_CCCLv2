def flipColumn(Square, Column):
    for i in range(len(Square)):
        if Square[i][Column] == "0":
            Square[i][Column] = "1"
        else: Square[i][Column] = "0"
    return Square

def flipRow(Square, Row):
    for i in range(len(Square)):
        if Square[Row][i] == "0":
            Square[Row][i] = "1"
        else: Square[Row][i] = "0"
    return Square

N = int(input())

Perfect_Sqaure = [["0" for i in range(N)] for i in range(N)]
Square = []
for i in range(N):
    line = input().split(" ")
    Square.append(line)

finish = False
count = 0
moves = []
if not finish:
    for row in range(N):
        one_in_row = 0
        for column in range(N):
            if Square[row][column] == "1":
                one_in_row += 1
            if one_in_row >= 2:
                Square = flipRow(Square, row)
                count += 1
                moves.append("R " + str(row + 1))
            if Square == Perfect_Sqaure:
                finish = True
                break
                break
#         print(one_in_row)
#
# print(Square)
if not finish:
    for column in range(N):
        one_in_column = 0
        for row in range(N):
            if Square[row][column] == "1":
                one_in_column += 1
            if one_in_column >= 2:
                Square = flipColumn(Square, column)
                count += 1
                moves.append("C " + str(column + 1))
            if Square == Perfect_Sqaure:
                finish = True
                break
                break
#         print(one_in_column)
# print(Square)

if not finish:
    print("-1")

else:
    print(count)
    for i in moves:
        print(i)