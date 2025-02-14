# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_value=0
        
        n=len(cardPoints)
        for i in range(n-k):
            sum_value+=cardPoints[i]
        left=0
        minvalue=sum_value
        for i in range(n-k,len(cardPoints)):
            sum_value+=cardPoints[i]
            sum_value-=cardPoints[left]
            left+=1
            minvalue=min(minvalue,sum_value)
            print("l",sum_value)
            print("lk",minvalue)
        print(minvalue)
        return sum(cardPoints)-minvalue
