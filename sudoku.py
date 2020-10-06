def getSudoku():
    print("THIS PROGRAM WILL SOLVE ANY SOLVABLE SUDOKU PUZZLE.")
    print("ENTER SUDOKU LINE BY LINE WITH NO SPACES BETWEEN NUMBERS")
    print("ENTER ZEROS FOR UNFILLED CELLS.")

    sudoku = []
    for i in range(9):
        line = input("Line %d: " %(i+1))
        while not line.isnumeric() or len(line) != 9:
            line = input("Line %d: " %(i+1))
        sudoku.append(list(map(int, line)))

    return sudoku

def printSudoku(sudoku):
    print("\n\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)

def findNext(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1

def isValid(sudoku, i, j, e):
    rowOk = all([e != sudoku[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3*(i//3), 3*(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False

def solveSudoku(sudoku, i=0, j=0):
    i, j = findNext(sudoku)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False

if __name__ == "__main__":
    sudoku = getSudoku()
    solveSudoku(sudoku, i=0, j=0)
    printSudoku(sudoku)




# hhhhhhhh
