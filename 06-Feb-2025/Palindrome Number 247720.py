# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False 
        left=-0
        right=len(str(x))-1
        x=str(x)
        while left < right:
            if x[left]!=x[right]:
                return False 
            left+=1
            right-=1
        return True