class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # by using the prefix sum algorthim we gona make two array and finally multiply them 
        count=0
        prefix=0
        hash_map={0:1}
        for i in range(len(nums)):
            ## the priinclple is simple 2 %5==2  and 22%5==2 so there is 5k length
            prefix+=nums[i]
            rem=prefix%k
            if rem in hash_map:
                count+=hash_map[rem]# the count is the summation of  hashmap [rem] it is prefix sum
                #it contains the sum of theprevious one
                
                hash_map[rem]+=1
            else:
                hash_map[rem]=1
        return count