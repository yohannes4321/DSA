# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        list_t=[]
        for i in range(len(arr),1,-1):
            index=arr.index(i)

            if index +1==i:
                continue
            if index!=0:
                list_t.append(index+1)
            list_t.append(i)
            arr[:index+1]=reversed(arr[:index+1])
            arr[:i]=reversed(arr[:i])
        return list_t

