
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtracking(start, list_t):
            if len(list_t) == k:
                res.append(list_t[:])  # Append a copy of list_t to result
                return
            for i in range(start, n + 1):
                list_t.append(i)
                backtracking(i + 1, list_t)
                list_t.pop()
        
        backtracking(1, [])
        return res