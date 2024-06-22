class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, prev):
            if index == len(s):
                return True
            for i in range(index, len(s)):
                value = int(s[index:i+1])
                if prev == value + 1 and dfs(i + 1, value):
                    return True
            return False

        for i in range(len(s) - 1):
            nums = int(s[:i + 1])
            if dfs(i + 1, nums):
                return True
        return False