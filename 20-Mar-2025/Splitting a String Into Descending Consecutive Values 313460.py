# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, st: str) -> bool:
        total=[]
        def backtrack(s,path):
            if len(path)>=2:
                if path[-1] != path[-2]-1:
                    return 
            if s=="":
                if len(path) > 1:
                    total.append(path[:])
                return 
                    
                
            for i in range(len(s)):
                to_left=int(s[:i+1])
                path.append(to_left)
                to_right=s[i+1:]
                backtrack(to_right,path)
                path.pop()
        backtrack(st,[])
        print(total)
        if len(total) <1:
            return False
        else :
            return True  
        