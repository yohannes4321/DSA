# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # In case k is greater than the length of the array

    # Reverse the entire array
        nums.reverse()

    # Reverse the first k elements
        nums[:k] = reversed(nums[:k])

    # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])

        return nums