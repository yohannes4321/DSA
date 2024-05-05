class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # Step 1: Sort the array
        count = 0
        left, right = 0, len(nums) - 1  # Step 2: Initialize pointers

        while left < right:  # Step 3: Count operations
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                count += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1

        return count  # Step 4: Return the count