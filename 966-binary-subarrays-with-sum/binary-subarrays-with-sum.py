class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count=0
        prefix=0
        freq={0:1}
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix-goal in freq:
                count+=freq[prefix-goal]
            if prefix not  in freq:
                freq[prefix]=1
            else :
                freq[prefix]+=1
        return count 
