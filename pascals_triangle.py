height = int(input("Enter desired height of Pascal\'s Triangle: "))

for row in range(0, height):
    if row == 0:
        curRow = [1]
        print(str(curRow))
    elif row == 1:
        curRow = [1,1]
        print(str(curRow))
    else:
        prevRow = curRow
        curRow = [1]
        for num in range(0,(len(prevRow) - 1)):
            curRow.append(prevRow[num] + prevRow[num+1])
        curRow.append(1)
        print(str(curRow))



