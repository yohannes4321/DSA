class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # now we are  not counting the number of element now we are cheaking the length greater than twoso when we intialize it we can intilaize at least it must have size of 2
        hash_map={0:-1}
        prefix_sum=0

        for i in range(len(nums)):
            prefix_sum+=nums[i]
            removal=prefix_sum % k 
            if removal in hash_map:
                if i - hash_map[removal]>=2:
                    return True 
            else:
                hash_map[removal] =i
        print(hash_map)
        return False

        