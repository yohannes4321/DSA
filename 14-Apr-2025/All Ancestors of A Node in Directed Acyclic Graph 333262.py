# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # write in adjcency list
        graph=[[] for _ in range(n)]
        all_ancestor=[[] for _ in range(n)]
        def dfs(i,visted):
            visted.add(i)
            
            for neighbour in graph[i]:
                if neighbour not in visted:
                    dfs(neighbour,visted)



        for i in edges:
            src,des = i
            graph[src].append(des)
        
        for i in range(n):
            visted=set()
            ancestor=[]
            if i not in visted:
                dfs(i,visted)
            for n in visted:
                if i ==n:
                    continue
                else:
                    # ancestor[n].append(i)
                    all_ancestor[n].append(i)
        return all_ancestor

