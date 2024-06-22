class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        def backtrack(index,comb):
            
            
            if len(comb)>=2 and comb[-1]<comb[-2]:
                return
            if len(comb)>=2:
                ans.add(tuple(comb[:]))
                 
            if index > len(nums):
                return
            for i in range(index,len(nums)):
                comb.append(nums[i])
                backtrack(i+1,comb)
                comb.pop()
            
        backtrack(0,[])
        return ans