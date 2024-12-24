class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # the array is postive integer so we use sliding window techinque and two pointer
        min_length=float('inf')
        sum_value=0
        left=0
        for right  in range(len(nums)):
            sum_value+=nums[right]
            while sum_value >= target:
                # now it is vallid so we gona cheack it 
                min_length=min(min_length,right-left+1)
                sum_value-=nums[left]
                left+=1
        if min_length == float('inf'):
            return 0
        else:
            return min_length
            



        