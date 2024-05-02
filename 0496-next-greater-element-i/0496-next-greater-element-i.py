class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map={nums:index for index,nums in enumerate (nums1)}
        res=[-1]*(len(nums1))
        stack=[]
        for i in range(len(nums2)):
            current=nums2[i]
            while stack and current > stack[-1]:# this show us that current value is greatter than hte stack top value and we use while loop to go from the top to bottom 
                n=stack.pop()
                ind=hash_map[n]
                res[ind]=current
                print(current)
            if current in hash_map:
                stack.append(current)
        return res
                
        