class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        def backtrack(res,nums,no_list,start ):
            res.append(no_list[:])
            for i in range(start,len(nums)):
                no_list.append(nums[i])
                backtrack(res,nums,no_list,i+1)
                no_list.pop()
                
                
             
        backtrack(res,nums,[],0)    
        return res
           
        
        
        