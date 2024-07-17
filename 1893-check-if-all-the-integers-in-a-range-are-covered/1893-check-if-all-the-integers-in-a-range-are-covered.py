class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            covered=False
            for left,right in ranges:
                if left<= i <=right:
                    covered=True
                    break
            if covered==False:
                return False
        return True
            