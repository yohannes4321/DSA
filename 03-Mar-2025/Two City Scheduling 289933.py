# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        nums2 = sorted(costs,key=lambda x:x[0]-x[1])
        cur=0
        print(nums2)
        for i in range(len(costs)//2):
            cur+=nums2[i][0]
        for i in range(len(costs)//2,len(costs)):
            cur+=nums2[i][1]
        return cur