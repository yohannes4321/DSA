class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_t=0
        res=0
        freq_sum={0:1}
        diff=0
        for i in nums:
            sum_t+=i
            diff = sum_t -k
            res+=freq_sum.get(diff,0)

            if sum_t in freq_sum:
                freq_sum[sum_t]+=1
            else:
                freq_sum[sum_t]=1
        return res

        