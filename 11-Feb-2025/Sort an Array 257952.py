# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # we gona use merge sort
        def merge(left_half,right_half):
            i,j=0,0
            temp=[]
            while i <len(left_half) and j<len(right_half):
                if left_half[i]<= right_half[j]:
                    temp.append(left_half[i])
                    i+=1
                else:
                    temp.append(right_half[j])
                    j+=1
            while i <len(left_half):
                temp.append(left_half[i])
                i+=1
            while j <len(right_half):
                temp.append(right_half[j])
                j+=1
            return temp    
        def mergesort(nums,left,right):
            if left==right:
                return [nums[left]]
            mid=(left+right)//2
            
            left_half=mergesort(nums,left,mid)
            right_half=mergesort(nums,mid+1,right)
            return merge(left_half,right_half)
            
        return mergesort(nums,0,len(nums)-1)    