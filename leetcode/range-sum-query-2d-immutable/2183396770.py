class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.prefix = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            row = matrix[i]
            prow = [0]*n 
            prow[0] = row[0]
            for i in range(1, n):
                prow[i] = prow[i-1]+row[i]
            if len(self.prefix)==0:
                self.prefix.append(prow)
            else:
                prev = self.prefix[-1]
                for k in range(len(prev)):
                    prow[k]+=prev[k]
                self.prefix.append(prow)
        # print(self.prefix)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.prefix[row2][col2]
        if row1==0:
            return self.prefix[row2][col2]-self.prefix[row2][col1-1]
        if col1==0:
            return self.prefix[row2][col2]-self.prefix[row1-1][col2]
        return self.prefix[row2][col2]-self.prefix[row1-1][col2]-self.prefix[row2][col1-1]+self.prefix[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)