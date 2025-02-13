class Solution:
    def validPalindrome(self, s: str) -> bool:
        count=0
        left=0
        right=len(s)-1
        is_count1=True
        is_count2=True
        while left < right:
            if s[left]!=s[right]:
                right-=1
                count+=1
                
            else:
                right-=1
                left+=1
        if count>1:
            is_count1=False
        count=0
        left=0
        right=len(s)-1
        while left < right:
            if s[left]!=s[right]:
                left+=1
                count+=1
            else:
                right-=1
                left+=1
        if count > 1:
            is_count2=False
        return is_count2 or is_count1
        



 
            

    
 