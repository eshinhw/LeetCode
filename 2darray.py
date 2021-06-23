from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.matrix = matrix
        col = len(matrix[0])
        row = len(matrix)
        self.partial_sum = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if j == 0:
                    self.partial_sum[i][j] = matrix[i][j]
                else:
                    self.partial_sum[i][j] = self.partial_sum[i][j-1] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total_sum = 0

        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                total_sum += self.matrix[i][j]

        return total_sum

matrix = [[1,2,3], [4,5,6], [7,8,9]]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(0,0,1,1)

