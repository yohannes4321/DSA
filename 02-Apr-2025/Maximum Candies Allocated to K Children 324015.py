# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def valid(mid):
            if mid == 0:
                return True

            count = 0
            for i in range(len(candies)):
                count+=candies[i]//mid

                # print("count",count)
                if count >= k:
                    # print("mid",mid )
                    # print("true")
                    return True

            return False
        l=0
        r=max(candies)

        while l <= r:
            mid=(l+r)//2
            if valid(mid):
                l=mid+1
            else:
                r=mid-1

        return r
        