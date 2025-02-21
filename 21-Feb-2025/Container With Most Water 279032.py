# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area between the lines at left and right pointers
            h = min(height[left], height[right])
            w = right - left
            area = h * w

            # Update the maximum area
            max_area = max(max_area, area)

            # Move the pointer with the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area