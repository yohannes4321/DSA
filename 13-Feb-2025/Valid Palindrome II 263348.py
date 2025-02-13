# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
       
        l,r=0,len(s)-1
        if len(s) < 3:
            return True

        while l<r:
            if s[l]!=s[r]:
                r_string = s[:r]+ s[r+1:]
                l_string = s[:l]+ s[l+1:]
                if l_string == l_string[::-1] or r_string == r_string[::-1]:
                    return True
                else:
                    return False
            l+=1
            r-=1
        return True

    
# abbab abba


