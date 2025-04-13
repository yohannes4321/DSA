# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bounds(row,col):
            return ((0 <= row < len(board)) and (0 <= col < len(board[0])))

        matrices=[[False for _ in range(len(board[0]))] for _ in range(len(board))]

        direction=[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row,col):
            matrices[row][col]=True
            board[row][col]='M'

            for row_dic,col_dic in direction:
                new_row=row+row_dic
                new_col=col+col_dic

                if bounds(new_row,new_col):
                    if board[new_row][new_col] == "O":
                        dfs(new_row,new_col)


        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row == 0 or col == 0 or col == len(board[0]) - 1 or row == len(board)-1): 
                    if board[row][col] == "O":
                        if not matrices[row][col]:
                            # print(row,col)
                            dfs(row,col)
        # print(board)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]=='M':
                    board[row][col]='O'
                else:
                    board[row][col]='X'
                
                    

        