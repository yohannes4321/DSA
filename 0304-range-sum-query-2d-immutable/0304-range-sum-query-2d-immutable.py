class NumMatrix:

    """def __init__(self, matrix: List[List[int]]):
        ROWS,COLS=len(matrix),len(matrix[0])
        self.sumMatrix=[[0] *(COLS+1) for r in range(ROWS +1 )]

        for r in range(ROWS):
            prefix=0 # for every line we must solve prefix of sum start from zero 
            for c in range(COLS):
                prefix += matrix[r][c]
                above= self.sumMatrix [r][c+1]
                self.sumMatrix[r+1][c+1]=prefix + above 

     

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2=row1 +1,col1+1,row2+1 ,col2+1
        bottomright=self.sumMatrix[r2][c2]
        left=self.sumMatrix[r1-1][c2]
        above=self.sumMatrix[r2][c1-1]
        lefttop=self.sumMatrix[r1-1][c1-1]
        return bottomright-left-above+lefttop"""
    def __init__(self,matrix: List[List[int]]):
        ROWS,COLS=len(matrix),len(matrix[0])
        self.sum_matrix=[[0]*(COLS+1) for r in range(ROWS+1)]

        # INTIALIZE THE SUM MATRIX 
        # THIS IS FOR THE FORMER MATRIX WHICH DOES NOT ADD THE LEFT AND RIGHT ZERO
        for r in range(ROWS) :
            prefix=0
            for c in range(COLS):
                prefix+=matrix[r][c]
                above=self.sum_matrix[r][c+1] # because it is not added
                self.sum_matrix[r+1][c+1]=prefix+above
    def sumRegion(self,row1,col1,row2,col2):
        r1,c1,r2,c2=row1+1,col1+1,row2+1,col2+1 
        thewholematrix=self.sum_matrix[r2][c2]
        leftmatrix=self.sum_matrix[r2][c1-1]
        abovematrix=self.sum_matrix[r1-1][c2]
        topleft=self.sum_matrix[r1-1][c1-1]

        return thewholematrix - leftmatrix - abovematrix + topleft





































# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)