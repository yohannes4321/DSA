class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_t=0
        hash_maps={0:1}
        res=0
        for n in nums:
            sum_t+=n
            reminder=sum_t%k
            if reminder in hash_maps:
                res+=hash_maps[reminder]
                hash_maps[reminder]+=1


            else:
                hash_maps[reminder]=1
        return res
                
                
                