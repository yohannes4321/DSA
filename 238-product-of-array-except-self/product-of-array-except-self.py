class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*(len(nums))
        prefix_mul=1
        suffix=1
        suff_ar=[1]*(len(nums))
        arr=[1]*len(nums)
        for i in range(len(nums)):
            prefix_mul*=nums[i]
            prefix[i]=prefix_mul
        for j in range(len(nums)-1,-1,-1):
            suffix*=nums[j]
            suff_ar[j]=suffix
        for k in range(len(nums)):
            arr[k] = (prefix[k - 1] * suff_ar[k + 1]) if (0 < k < len(nums) - 1) else (suff_ar[k + 1] if k == 0 else prefix[k - 1])

        return arr

