class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_t=""
        word=strs[0]
        for i in range(len(word)):
            for j in range(1,len(strs)):
                if i == len(strs[j]) or word[i]!= strs[j][i]:
                    return str_t
            str_t+=word[i]
         
        return str_t




                