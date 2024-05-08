class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map={value:key for key ,value in enumerate(nums1)}
        stack=[]
        res=[-1]*len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                n=stack.pop()
                index=hash_map[n]
                res[index]=nums2[i]
                
            if nums2[i] in hash_map:
                stack.append(nums2[i])
            
        return res
    
    