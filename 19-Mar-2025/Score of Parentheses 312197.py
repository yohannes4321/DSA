# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(score)
                score=0
            else:
                score=stack.pop()+max(1,2*score)
        return score
            
            
            
