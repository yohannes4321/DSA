class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        sum_t=0
        max_value = float('-inf')  
        for right in range(len(nums)):
            sum_t+=nums[right]
            
            if right-left+1==k:
             
               
                max_value=max(max_value,sum_t/k)
                sum_t-=nums[left]
                left+=1
                    
        return max_value
                
            