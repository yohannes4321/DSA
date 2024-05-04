class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()  # Sort the people's weights in ascending order
        left, right = 0, len(people) - 1
        count = 0

        while left <= right:
            # Check if the sum of weights at the current pointers is within the limit
            if people[left] + people[right] <= limit:
                count += 1
                left += 1
                right -= 1
            # If the weight at the left pointer exceeds the limit, move the left pointer
            elif people[left] >= limit:
                count += 1
                left += 1
            # Otherwise, move the right pointer
            else:
                count += 1
                right -= 1

        return count