class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findleft(nums,target):
            index=-1
            left,right=0,len(nums)-1
            
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    index=mid
                    right=mid-1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return index
        def findright(nums,target):
            index=-1
            left,right=0,len(nums)-1
            
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    index=mid
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return index
        l=findleft(nums,target)
        r=findright(nums,target)
        return[l,r]
            
            
         
        
        
               