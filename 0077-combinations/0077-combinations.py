class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtrack (empty_list,start):
            
            if len(empty_list)==k:
                res.append(empty_list[:])
                return 
                
           
            for i in range(start,n+1):
                empty_list.append(i)
                backtrack(empty_list,i+1)
                empty_list.pop()
            
        backtrack([ ],1)
        return res