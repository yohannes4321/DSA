# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #  the idea is if the number is not add to it not equal to 10 just add 
        # if not add 1 infront on the 0 index and make the rest equal to 0
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+1!=10:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
                if i==0:
                    return [1] + digits