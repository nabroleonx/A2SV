class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.prefix = [[0]*(m+1)]
        for row in matrix:
            prefix_row = [0]
            for j in row:
                prefix_row.append(prefix_row[-1]+j)
            self.prefix.append(prefix_row)
       
        
        for j in range(m+1):
            for i in range(1, n+1):
                self.prefix[i][j] += self.prefix[i-1][j]
        
        print(self.prefix)
        
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row2+1][col1] - self.prefix[row1][col2+1] + self.prefix[row1][col1]
    
    '''
    [[0, 0, 0, 0, 0, 0], 
    [0, 3, 3, 4, 8, 10], 
    [0, 8, 14, 18, 24, 27], 
    [0, 9, 17, 21, 28, 36], 
    [0, 13, 22, 26, 34, 49], 
    [0, 14, 23, 30, 38, 58]]
    
    
    
    
    [
        [3,  3,  4,  8,  10], 
        [8,  14, 18, 24, 27], 
        [9,  17, 21, 28, 36], 
        [13, 22, 26, 34, 49], 
        [14, 23, 30, 38, 58]
    ]

    
    '''


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)