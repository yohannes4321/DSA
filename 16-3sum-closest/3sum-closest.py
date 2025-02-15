from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sorting the list first
        closest_sum = float('inf')  # Store closest sum
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find an exact match, return immediately
                if current_sum == target:
                    return target
                
                # Update closest sum if this is closer than before
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum  # Return the closest sum found
