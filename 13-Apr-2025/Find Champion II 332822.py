# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # [0,1,2,3]
        # [0,0,0,0]
        hash_set=set()
        graph =[[] for _ in range(n)]
        for i in edges:
            src,des=i
         
            hash_set.add(des)
        
        if len(hash_set)!=n-1:
            return -1
        else:
            for i in range(n):
                if i not in hash_set:
                    return i
        hash_set=set()
