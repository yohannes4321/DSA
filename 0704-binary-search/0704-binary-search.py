class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
         
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid
                #include if greater or equal to both case
        return right if nums[right]==target else -1       
                
         