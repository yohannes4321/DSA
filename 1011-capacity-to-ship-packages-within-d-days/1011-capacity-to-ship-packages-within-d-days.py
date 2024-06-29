class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the first idea to range of value min and max capacity
        
        def no_days( capacity,weights):
            load=0
            day=1
            for i in   range(len(weights)):
                if weights[i]+load >capacity:
                    day+=1
                    load=weights[i]
                else:
                    load+=weights[i]
            return day  
        left=max(weights)
        right=sum(weights)
        while left <= right :
            mid=(left+right)//2
            if no_days(mid,weights)<=days:
                right=mid-1
            else:
                left=mid+1
        return left        
        
        
                
                
                
                
            