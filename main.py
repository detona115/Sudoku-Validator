# This is a simple Python script who aim to validate a sudoku grid.
# This approach consists in doing two validations
# The first by checking each block and the last by checking rows and columns

def validSolution(board):
    if not isinstance(board, list):
        return False

    if validBlocks(board) and validBoard(board) is True:
        return True

    return False


def validBlocks(bord):
    # this function meant to test each block (3x3) of the board
    # in the case where one block has empty space or duplicate number
    # the function return False otherwise True
    minimum = 0
    maximum = 3
    row = 3
    block = []
    positions = []
    while row < 10:
        # this loop traverse each block (3x3) of the board, 3 blocks per loop
        # and test if each block is valid or not

        positions = [(x, y) for x in range(minimum, row) for y in range(maximum)]
        block.clear()
        for x, y in positions:
            block.append(bord[x][y])
        # print(block)
        if len(set(block)) != len(block) or 0 in block:
            print(f'This block => {block} is invalid')
            return False

        positions = [(x, y) for x in range(minimum, row) for y in range(maximum, maximum + 3)]
        block.clear()
        for x, y in positions:
            block.append(bord[x][y])
        # print(block)
        if len(set(block)) != len(block) or 0 in block:
            print(f'This block => {block} is invalid')
            return False

        positions = [(x, y) for x in range(minimum, row) for y in range(maximum + 3, maximum + 6)]
        block.clear()
        for x, y in positions:
            block.append(bord[x][y])
        # print(block)
        if len(set(block)) != len(block) or 0 in block:
            print(f'This block => {block} is invalid')
            return False

        minimum = row
        row = row + 3

    return True


def validBoard(bord):
    # This function meant to validate the board
    # checking line by line, column by column
    # if there is no duplicated value

    # checking each line
    for i in bord:
        if len(set(i)) != len(i) or 0 in i:
            print(f'This line => {i} is invalid')
            return False

    col = []
    # checking each column
    for x in range(0, 9):
        for i in bord:
            col.append(i[x])
        if len(set(col)) != len(col) or 0 in col:
            print(f'This column => {col} is invalid')
            return False
        col.clear()

    return True


if __name__ == '__main__':

    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

    board2 = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 0, 3, 4, 8],
        [1, 0, 0, 3, 4, 2, 5, 6, 0],
        [8, 5, 9, 7, 6, 1, 0, 2, 0],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 0, 1, 5, 3, 7, 2, 1, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 0, 0, 4, 8, 1, 1, 7, 9]
    ]
    print(validSolution(board))

