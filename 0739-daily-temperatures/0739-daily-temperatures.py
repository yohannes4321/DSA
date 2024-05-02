class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Initialize an empty stack to keep track of indices
        res = [0] * len(temperatures)  # Initialize the result list with zeros

        for i in range(len(temperatures)):
            current = temperatures[i]

            # Pop elements from the stack while the current temperature is greater
            # than the temperature at the top of the stack
            while stack and current > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index

            # Push the current index onto the stack
            stack.append(i)

        return res
