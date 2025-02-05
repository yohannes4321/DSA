# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")
        result=[]
        for word in words:
            word1=set(word.lower())
            if word1 <= row1 or word1 <= row2 or word1 <= row3:
                result.append(word)
        return result