from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[0] *(len(graph))
        queue=deque()
        def bfs(i):
            queue.append(i)
            color[i]=1
            while queue:
                node=queue.popleft()
                for neigh in graph[node]:
                    print(neigh)
                    if color[neigh]==0:
                        color[neigh]=- color[node]
                        queue.append(neigh)
                    elif color[neigh]== color[node]:
                        print("gorbert",color[neigh])
                        print("real node",color[node])
                        return False
            return True
                
        for i in range(len(graph)):
            if color[i] ==0:
                if not bfs(i):
                    return False
        return True
