class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[1]* len(nums)
        #for prefix
        prefix=1
        for i in range(len(nums)):
            
            output[i]=prefix
            prefix*=nums[i]
            #  i have modifyed the predix by multiplying the prefix with current num
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            
            output[i]*=suffix
            suffix*=nums[i]
        return output