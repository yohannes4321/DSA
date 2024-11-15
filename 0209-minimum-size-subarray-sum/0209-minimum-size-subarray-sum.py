class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        min_length=float('inf')
        sum_t=0
        for r in range(len(nums)):
            sum_t+=nums[r]
            while sum_t>=target:
                min_length=min(min_length,r-left+1)
                sum_t-=nums[left]
                left+=1
             
            
        return min_length if min_length!=float('inf') else 0 
                
#max_length we gona calculate after while loop maxlength
#min_length we gona calculate inside while loop frist before increasing the left index ;