class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
         
        # Create a dictionary to store next greater elements
        next_greater = {}
        stack = []

        # Iterate through nums2
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Set remaining elements in the stack to -1
        while stack:
            next_greater[stack.pop()] = -1

        # Find next greater elements for nums1
        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1))

        return result

    