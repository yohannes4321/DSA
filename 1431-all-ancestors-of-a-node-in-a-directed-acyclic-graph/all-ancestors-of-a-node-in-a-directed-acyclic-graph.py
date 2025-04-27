from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:      
        queue=deque()
        adj_list=[[] for _ in range(n)]
        indegree=[0] * n
        for src,des in edges:
            adj_list[src].append(des)
            indegree[des]+=1
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        pre=[set() for _ in range(n)]
        while queue:
            node=queue.popleft()
            for neigh in adj_list[node]:
                pre[neigh] |= pre[node]
                pre[neigh].add(node)
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        r=[]
        for s in pre:
            r.append(sorted(list(s)))
        return r