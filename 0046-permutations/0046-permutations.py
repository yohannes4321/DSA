class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # we gona use backtracking
        res =[]
        def backtrack(index,per):
            if len(per)==len(nums):
                res.append( per[:]) 
                return
            for i in range(len(nums)):
                if  not nums[i] in per:
                    per.append(nums[i])
                    backtrack(i+1 ,per)
                    per.pop()
                
        backtrack(0,[])
        return res