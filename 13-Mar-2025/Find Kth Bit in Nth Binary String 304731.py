# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return "0"
        mid=(2**n-1)//2 +1
        if k==mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n-1,k)
        else:
            return "1" if self.findKthBit(n-1,2**n -k)=="0" else "0"

        
