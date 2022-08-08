def exist(board, word):
    visit = set()

    def check(i, j, counter):
        if counter == len(word) - 1 and board[i][j] == word[counter]:
            return True
        elif counter == len(word) - 1 and board[i][j] != word[counter]:
            return False
        counter += 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r, c in directions:
            row, col = i+r, j+c
            if (row in range(len(board)) and
                col in range(len(board[row])) and
                counter <= len(word) - 1 and
                    board[row][col] == word[counter] and
                    (row, col) not in visit):
                print(board[row][col])
                visit.add((row, col))
                if check(row, col, counter):
                    return True
                visit.remove((row, col))

    for i in range(len(board)):
        for j in range(len(board[i])):
            visit.clear()
            if board[i][j] == word[0]:
                visit.add((i, j))
                if check(i, j, 0):

                    return True
    return False


# Bug
print(exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
            "ABCESEEEFS"))

# TLE
# [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
# "AAAAAAAAAAAABAA"
