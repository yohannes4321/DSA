# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left < right:

            
            middle=(left+right)//2
            print("mid",middle)
            if nums[middle] > target:
                right=middle-1
            elif nums[middle] < target:
                left=middle+1
            elif nums[middle]==target:
                print("d",middle)
                return middle 
        return -1
           
