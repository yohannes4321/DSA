# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # make adj list
        number=0
        visted=set()
        result=[]
        graph=[[] for _ in range(n)]
        for i in edges:
            src,des=i
            graph[src].append(des)
            graph[des].append(src)
        def dfs(i,visted,graph,result):
            #length of nodes
            visted.add(i)
            result.append(i)
            for nehbour in graph[i]:
                if nehbour not in visted:
                    dfs(nehbour,visted,graph,result)
        
        for i in range(n):
            edge=0
            if i not in visted:
                result=[]
                dfs(i,visted,graph,result)
                 
                for i in result:
                    edge+=len(graph[i])
                number_edge=edge//2
                 
                if (len(result)*(len(result)-1))//2== number_edge:
                    number+=1
                    
        return number

 


