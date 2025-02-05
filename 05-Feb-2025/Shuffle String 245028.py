# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        list_t=['']*len(s)
        for i ,index in enumerate(indices):
            list_t[index]=s[i]
        return "".join(list_t)
