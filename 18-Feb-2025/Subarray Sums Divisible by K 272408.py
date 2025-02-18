# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq={0:1}
        prefix=0
        count=0
        for i in range(len(nums)):
            prefix+=nums[i]
            print("p",prefix)
            if (prefix % k) in freq:
                print(prefix)
                count+=freq[prefix % k]
            if prefix%k in freq:
                freq[prefix%k]+=1
            elif prefix%k not in freq:
                freq[prefix%k]=1
        return count
            
        