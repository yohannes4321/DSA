class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
            #KJJ
        else:
            str_t=str(x)
            left=0
            right =len(str_t)-1
            while left <right:
                if str_t[left]!=str_t[right]:
                    return False
                left+=1
                right-=1
            return True