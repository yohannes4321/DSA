class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[ ]
        nums.sort()
        def backtrack(nums,res,empty_list,start):
            if empty_list not in res:
             
                res.append( empty_list[:]) #we want to copy 
            for i in range(start,len(nums)):
                 
                    empty_list.append(nums[i])
                    backtrack(nums,res,empty_list,i+1)
                    empty_list.pop()

        backtrack(nums,res,[],0)
        return res 