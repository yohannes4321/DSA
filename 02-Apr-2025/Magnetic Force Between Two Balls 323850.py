# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position=sorted(position)
        low=1
        high=max(position)-min(position)

        def predicator(value):
            number_balls=1
            intial_position=position[0]
            # if number_balls >= m:
            #     return True
            for i in range(1,len(position)):
                if position[i]-intial_position >= value:
                    intial_position=position[i]
                    number_balls+=1
            if number_balls >= m:
                return True
            return False       
        while low <= high:
            mid=(low+high)//2
            if predicator(mid):
                low=mid+1
            else:
                high=mid-1
        return high

 
            

