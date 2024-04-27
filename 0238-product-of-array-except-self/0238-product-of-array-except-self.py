class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # i am gona use two array the prefix and suffix array
 
        prefix=1
        suffix =1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=prefix
            prefix *=nums[i]
        for j in range(len(nums)-1,-1,-1): # backward going in reaverse diraction 
            res[j]*=suffix # to replace it (we donot want to overwrite it ) we want it  to multiply and put  the product in the postion 
            suffix*=nums[j]
        return res
            