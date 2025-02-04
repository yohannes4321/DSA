# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = Counter(nums)
        # res=[]
        # arr = list(freq.keys())
        # arr.sort(key = lambda x : -freq[x])

        # for i in range(k):
        #     res.append(arr[i])

        # return res
        freq=Counter(nums)
        res=[]
        number_element=list(freq.keys())
        number_element.sort(key=lambda x: freq[x],reverse=True)
        print(number_element)
        for i in range(k):
            res.append(number_element[i])
        return res