# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        string=""
        i=0
        num=0
        while i < len(s):
            if s[i].isalpha():
                string+=s[i]
                i +=1
            elif s[i].isdigit():
                num=num*10+int(s[i])
                i+=1
            else:
                opening=1
                j=i+1
                while opening and  j < len(s) :
                    if s[j]=='[':
                        opening+=1
                    elif s[j] ==']':
                        opening-=1
                    j+=1
                temp=self.decodeString(s[i+1:j-1])
                new_temp=temp*num
                string+=new_temp
                num=0
                i=j
        return string


        
            
        