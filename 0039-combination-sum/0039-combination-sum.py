class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, temp, total):
            # If the total equals the target, add a copy of temp to the result
            if total == target:
                res.append(temp[:])
                return
            # If the total exceeds the target, return to stop further processing
            if total > target:
                return
            
            # Iterate over the candidates starting from the current index
            for i in range(start, len(candidates)):
                # Include the current candidate
                temp.append(candidates[i])
                # Recursively call backtrack with updated total and temp
                backtrack(i, temp, total + candidates[i])
                # Exclude the current candidate to explore other possibilities
                temp.pop()
        
        # Start the backtracking with an empty list and total 0
        backtrack(0, [], 0)
        return res