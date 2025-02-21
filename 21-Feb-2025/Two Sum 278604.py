# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap={} # value,index
        # we have made addtional place space-complexity -> big(n )
        # in premap value :index so preva[value] gives as index 
        for index,value in enumerate(nums):
            diff=target-value
            if diff  in premap:
                return [premap[diff],index]
            else:
                premap[value]=index
                #####