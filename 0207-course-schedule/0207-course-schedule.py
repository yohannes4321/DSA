from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue=deque()
        adj_list=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for des,src in prerequisites:
            adj_list[src].append(des)
            # adj_list[des].append(src)
            indegree[des]+=1
            # indegree[src]+=1
        # print(indegree)
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)

        res=[]
        while queue:
            node=queue.popleft()
            res.append(node)
            # print(res)

            for neigh in adj_list[node]:
                indegree[neigh]-=1
                # indegree[node]-=1
                # print("in",indegree[neigh])
                if indegree[neigh]==0:
                    queue.append(neigh)
        # print(res)
        if len(res)!=numCourses:
            return False
        else:
            return True
