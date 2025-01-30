class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        out = []
        for i in s:
            if i.isalnum():
                out.append(i)
        return out == out[::-1]
