# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def validator(time):
            res=0
            for i in range(len(ranks)):
                no_cars=int(math.sqrt(time /ranks[i]))
                res+=no_cars
            if res>=cars:
                return True
            else :
                return False
        low=1
        high=(max(ranks))*(cars**2)
        print("high",high)
        while low <=high:
            mid=(low+high)//2

            if validator(mid):
                high=mid-1
            else:
                low=mid+1
        return low

        