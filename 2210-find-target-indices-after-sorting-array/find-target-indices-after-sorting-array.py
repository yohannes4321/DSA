class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        list_t=[]
        for i in range(len(nums)):
            if nums[i]==target:
                list_t.append(i)
        return list_t