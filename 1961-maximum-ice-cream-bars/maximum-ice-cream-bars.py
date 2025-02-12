class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sum_value=0
        costs=sorted(costs)
        total=0
        for i in range(len(costs)):
            if total+costs[i]<=coins:
                total+=costs[i]
            
                sum_value+=1
                 
        return sum_value
