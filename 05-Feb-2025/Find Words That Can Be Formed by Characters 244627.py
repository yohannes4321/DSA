# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dict_t=Counter(chars)
        length=0
        for word in words:
            word_count=Counter(word)
            print(word_count)
            print(dict_t)
            if word_count <= dict_t:
                length+=len(word)
            
        return length