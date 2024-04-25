class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # here we gona add the value here only the summation is box 
        row=len(matrix) # to add 0s on the top    ###$$$$  this is for res the list we have created 
        column=len(matrix[0])# to add 0s on the left
        #createing a res
        self.res=[[0]*(column +1) for _ in range(row+1)]
        for i in range(len(matrix)):
            linesum=0
            for j in range(len(matrix[0])): 
                linesum+=matrix[i][j] # the summmation of the line only there is no above 
                above=self.res[i][j+1]
                self.res[i+1][j+1]=linesum+above
 
                
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2= row1+1,col1+1,row2+1,col2+1 # this is for res list we increment 1
        abovee=self.res[row1-1][col2]
        left=self.res[row2][col1-1]
        bottomright=self.res[row2][col2]
        intersection=self.res[row1-1][col1-1]
        return bottomright-abovee-left+intersection


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)