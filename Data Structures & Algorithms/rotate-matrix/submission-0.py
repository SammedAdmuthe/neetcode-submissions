class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''

            1 3
            2 4
            0, 0 -> 0, 2
        '''


        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(m):
            for j in range(n//2 ):
                    matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
