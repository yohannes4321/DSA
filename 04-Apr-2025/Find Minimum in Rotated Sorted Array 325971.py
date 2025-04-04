# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        ans=float('inf')
        high=len(nums)-1
        while low <= high:
            
            mid=(low+high)//2
            
            ans=min(ans,nums[mid])
            print(ans)
            if nums[mid] > nums[high]:
                low=mid+1
            else:
                high=mid-1
            
        return ans