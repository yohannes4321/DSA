# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap_c=nums
        heapq.heapify(self.heap_c)



    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap_c,val)
        while len(self.heap_c)>self.k:
            heapq.heappop(self.heap_c)
        
        return self.heap_c[0]


        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)