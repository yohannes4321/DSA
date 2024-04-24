class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #let assume that the first string is shortes from all and if it termainates all 
        #will terminate f
        res=""
        for i in range(len(strs[0])):#let assume for this time that the first string is shortes of all if not we will check it later
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[0][i]!=strs[j][i]:
                    return res
            res+=strs[0][i]
        return res