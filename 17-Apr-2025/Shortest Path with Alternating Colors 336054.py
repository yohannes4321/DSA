# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        blue_edges=[[] for _ in range(n)]
        red_edges=[[] for _ in range(n)]
        queue=deque()
        visted=set()
        ans=[-1 for _ in range(n)]

        for i in redEdges:
            src,des=i
            red_edges[src].append(des)
        for j in blueEdges:
            src,des=j
            blue_edges[src].append(des)
        queue.append([0,0,'RED'])#node length prev_color
        visted.add((0,'RED'))# node color

        queue.append([0,0,'BLUE'])
        visted.add((0,'BLUE'))


        while queue:
          
            for _ in range(len(queue)):
                
                node,length,color=queue.popleft()
            
                if ans[node]==-1:
                    ans[node]=length
                if color == 'RED':
                    for neig in blue_edges[node]:
                        if (neig,'BLUE') not in visted:
                            visted.add((neig,'BLUE'))
                            queue.append((neig,length+1,"BLUE"))
                if color =='BLUE':
                    for neig in red_edges[node]:
                        if(neig,'RED') not in visted:
                            visted.add((neig,'RED'))
                            queue.append((neig,length+1,"RED"))
        return ans




