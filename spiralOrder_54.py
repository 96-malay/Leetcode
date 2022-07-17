
def spiralOrder(matrix):

    ans = []
    visit = set()
    row, col = 0, 0
    size = min(len(matrix), len(matrix[0])) // 2
    while row <= size:
        #           left to right
        i = row
        for j in range(col, len(matrix[i])-col):
            if (row, j) in visit:
                return ans
            ans.append(matrix[i][j])
            visit.add((row, j))
#           top to bottom
        for i in range(row+1, len(matrix)-row):
            if (i, j) in visit:
                return ans
            ans.append(matrix[i][j])
            visit.add((i, j))
        # i-=1

#           right to left
        k = j-1
        for k in range(j-1, col-1, -1):
            if (i, k) in visit:
                return ans
            ans.append(matrix[i][k])
            visit.add((i, k))

#           bottom to up
        if k >= 0:
            for l in range(i-1, row, -1):
                if (l, k) in visit:
                    return ans
                ans.append(matrix[l][k])
                visit.add((l, k))

        row += 1
        col += 1

    return ans
