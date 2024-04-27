class Solution(object):
    def subarraySum(self, nums, k):
        # i am gona use hashmap
        hash_map={0:1} # intilazing the hash_map with sum of 0 and frequancy of 1
        sum_t=0
        counter=0
        for i in range(len(nums)):
            sum_t+= nums[i]
            complement=sum_t-k
            if complement in hash_map:
                
                counter+=hash_map[complement]
            hash_map[sum_t]=hash_map.get(sum_t,0)+1            
        return counter