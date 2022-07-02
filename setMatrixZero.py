def setZeroes(matrix):
        """
        73. Set Matrix Zeroes
        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
        You must do it in place.
        """
        row=[]
        col=[]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j]=0
        print(matrix)
setZeroes([[1,1,1],[1,0,1],[1,1,1]])