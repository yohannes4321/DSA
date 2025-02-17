# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0:1}
        prefix = 0
        count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            to_be_removed = prefix - k
            if to_be_removed in map:
                count += map[to_be_removed]
            if prefix not in map:
                map[prefix] = 1
            else:
                map[prefix]+=1
        return
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict_t={0:1}
        count=0
        prefix_sum=0

        for i in range(len(nums)):
            prefix_sum+=nums[i] 
            if prefix_sum-k in dict_t:
                count+=dict_t[prefix_sum-k]
            if prefix_sum in dict_t:
                dict_t[prefix_sum]+=1
            else:
                dict_t[prefix_sum]=1
        return count


