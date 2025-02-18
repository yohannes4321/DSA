# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # i, j = 0, 0
        # result = []
        
        # while i < len(firstList) and j < len(secondList):
        #     # Find the intersection of firstList[i] and secondList[j]
        #     start = max(firstList[i][0], secondList[j][0])
        #     end = min(firstList[i][1], secondList[j][1])
            
        #     if start <= end:  # Only add if there is an actual intersection
        #         result.append([start, end])
            
        #     # Move the pointer of the interval that ends first
        #     if firstList[i][1] < secondList[j][1]:
        #         i += 1
        #     else:
        #         j += 1
        
        # return result
        i,j=0,0
        list_t=[]
        while i <len(firstList) and j<len(secondList):
            start=max(firstList[i][0],secondList[j][0])
            end=min(firstList[i][1],secondList[j][1])
            if start <= end:
                list_t.append([start,end])
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return list_t
             
 

 