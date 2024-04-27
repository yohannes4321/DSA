class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # this is easy solution but its vertual or conceptual
        left=0
        count=0
        max_length=0
        for right in range(len(nums)):
            # our goal isnot replacing the 0 to 1 but return max length  be smart
            if nums[right]==0:
                count+=1
            while count >k:
                
                
                
                #### in this when it searches for zero when it donot found left index must increase so outside the if statement incremant left index
                if nums[left]==0: # it s conceputall we repalce 0 to 1 but not actually our goal is lenghth
                    count-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length 
            