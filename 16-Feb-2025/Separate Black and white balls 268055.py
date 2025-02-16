# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        seeker=0
        holder=0
        count=0
        s=list(s)
        print(s)
        if s == sorted(s):
            return 0
        while seeker< len(s):
            if s[seeker]=='0'   :
                if s[seeker]!=s[holder]:

                 
                    s[seeker],s[holder]=s[holder],s[seeker]
                    count+= seeker-holder
                
                
                holder+=1
            seeker+=1
        return count 

        