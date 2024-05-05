class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <0:
            return False
        left =0
        right =int(sqrt(c))
        while (left <= right ):
            squ=left * left + right * right
            if squ == c:
                return True
            elif squ < c:
                left +=1
            elif squ > c :
                right -=1
            else :
                return False 
        
            
        