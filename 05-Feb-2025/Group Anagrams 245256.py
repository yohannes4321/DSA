# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_t={}
        for value in strs:
            val=str(sorted(value))
            if val not in dict_t:
                dict_t[val]=[value]
            else:
                dict_t[val].append(value)
        return list(dict_t.values())