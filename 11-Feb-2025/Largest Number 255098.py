# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numsStr = [str(nums[i]) for i in range(len(nums))]
        def comprator(a,b):
            val1=a+b
            val2=b+a
            if val1 > val2:
                return -1
            elif val2< val1:
                return 1
            else:
                return 0

        numsStr.sort(key = cmp_to_key(comprator))
        
        return str(int("".join(numsStr)))