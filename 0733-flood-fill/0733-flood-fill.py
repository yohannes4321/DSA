from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue=deque()
        visted=[[False for _ in range( len(image[0]))] for _ in range(len(image))]
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        def bound(row,col):
            return 0 <=row< len(image) and 0 <=col <len(image[0])
        def bfs(sr,sc):
            queue.append((sr,sc))
            first1=image[sr][sc]
            image[sr][sc]=color
            visted[sr][sc]=True

            while queue:
                row,col=queue.popleft()
                for add_row,add_col in direction:
                    new_row=row+add_row
                    new_col=col+add_col
                    if bound(new_row,new_col) and not visted[new_row][new_col] and image[new_row][new_col]==first1 :
                        image[new_row][new_col]=image[row][col]
                        queue.append((new_row,new_col))
                        visted[new_row][new_col]=True

        bfs(sr,sc)
        return image
        