import pandas as pd

input = "[1, 0, 0], [0, 1, 1], [1, 1, 0]:2"
input2 = "[[1, 0, 0], [0, 1, 1], [1, 1, 0]]:2"


def proccess_input(input):
    params = input.split(":")
    params[0] = convertStringInList(input)
    params[1] = params[1]

    return board_next_step(params[0], params[1])


def convertStringInList(word):
    matriz = []
    sublist = []
    for i in range(0, len(word)):
        if word[i] == "]":
            matriz.append(sublist)
            sublist = []
        elif word[i].isnumeric():
            sublist.append(word[i])
    return matriz


def board_next_step(initial_board, steps):
    count = 0
    nextboard = []

    for list in initial_board:
        nextboard.append(list.copy())

    while count < int(steps):
        aux = []

        for list in nextboard:
            aux.append(list.copy())

        for i in range(0, len(aux)):
            for j in range(0, len(aux[0])):
                state = aux[i][j]

                neighbors = countNeighbors(aux, i, j)

                if state == '0' and neighbors == 3:
                    nextboard[i][j] = '1'
                elif state == '1' and (neighbors < 2 or neighbors > 3):
                    nextboard[i][j] = '0'
                else:
                    nextboard[i][j] = state

        count = count + 1

    result = ""

    for list in nextboard:
        for i in list:
            result = result + i

    return ", ".join(result)
    # return nextboard


def countNeighbors(grid, x, y):
    numberRows = len(grid)
    numberCols = len(grid[0])

    sum = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            row = (x + i + numberRows) % numberRows
            col = (y + j + numberCols) % numberCols

            if abs(col - y) < 2:
                if abs(row - x) < 2:
                    sum = sum + int(grid[row][col])
    sum = sum - int(grid[x][y])
    return sum


print(pd.DataFrame(convertStringInList(input)))

print(proccess_input(input))
