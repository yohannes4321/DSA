class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum=0
        list_t=[]
        for i in nums:
            cur_sum+=i
            list_t.append(cur_sum)
        return list_t