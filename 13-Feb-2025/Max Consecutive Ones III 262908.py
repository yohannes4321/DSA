# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        running_sum=0
        max_length=0
        for right in range(len(nums)):
            running_sum+= nums[right]
            length=right-left+1
            num_zeros=length-running_sum
            
            while num_zeros > k:

                if nums[left]==1:
                    running_sum-=1
                
                left+=1
                length=right-left+1
                num_zeros=length-running_sum
            max_length=max(max_length,right-left+1)
        return max_length
                

                
            
        
            

