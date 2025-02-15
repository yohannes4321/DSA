list_t=[]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        list_t=set()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]+nums[i]==0:
                    list_t.add(tuple([nums[left],nums[right],nums[i]]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right]+nums[i] <0:
                    left+=1
                elif   nums[left]+nums[right]+nums[i]>0:
                    right-=1
        return list(list_t)
            
