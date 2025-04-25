from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue=deque()
        #bulild the graph and indegree
        
        in_degree=[0]* numCourses
        adj_list=[[] for _ in range(numCourses)]
        for i in prerequisites:
            des,src=i
            adj_list[src].append(des)
            in_degree[des]+=1
        # check the 0 indegree
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        # in the queue
        res=[]
        while queue:
            node=queue.popleft()
            res.append(node)
            for neigh in adj_list[node]:
                in_degree[neigh]-=1
                if in_degree[neigh]==0:
                    queue.append(neigh)
        if len(res)!=numCourses:
            return []
        else:
            return res


        