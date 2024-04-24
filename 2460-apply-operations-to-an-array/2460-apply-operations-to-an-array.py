class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        j=0
        for i in range(len(nums)):
            if i+1 < len(nums) and  nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
         
        zero =nums.count(0)
        nums=[i for i in nums if i !=0]
        nums=nums+[0]*zero
        return nums
        
                
            