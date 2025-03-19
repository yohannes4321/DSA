# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def dfs(l,r,alice):
            if l >r:
                return 0
            res= -inf if alice else inf
            if alice:
                res=max((nums[l]+dfs(l+1,r,not alice)),nums[r]+dfs(l,r-1,not alice))
            else:
                res=min((dfs(l+1,r,not alice)),(dfs(l,r-1,not alice)))
            return res
        return dfs(0,len(nums)-1,True)>=sum(nums)/2

        