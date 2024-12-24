class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix=0
        count=0
        hash_map={0:1}

        for i in range(len(nums)):
            prefix+=nums[i]
            removable=prefix % k
            if removable in hash_map:
                count+=hash_map[removable]
            if removable not in hash_map:
                hash_map[removable]=1
            elif removable in hash_map:
                hash_map[removable]+=1
        return count 

            
            