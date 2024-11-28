class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hash_set={0:1}
        sum_t=0
        res=0
        for i in nums:
            sum_t+=i
            reminder=sum_t %k
            if reminder in hash_set:
                res+=hash_set[reminder]
                hash_set[reminder]+=1
            else:
                hash_set[reminder]=1
        return res
            


            