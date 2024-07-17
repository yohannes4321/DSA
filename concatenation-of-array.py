class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        rs=[]
        for i in range(2*n):
            rs.append(nums[i%n])
        return rs    
            
