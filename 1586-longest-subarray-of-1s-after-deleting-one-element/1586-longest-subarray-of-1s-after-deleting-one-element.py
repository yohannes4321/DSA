class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Input: nums = [1,1,0,1]
        # Output: 3
        # Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1'
        

        left=0
        max_length=0
        zeros=0
        for right in range(len(nums)):
            if nums[right ] == 0:
                zeros+=1
            # we have to remove till only one element for zeros we use while 
            while zeros > 1:
                
                if nums[left] == 0:
                    zeros -= 1
                left+=1
            max_length=max(max_length,right-left)
        return max_length


