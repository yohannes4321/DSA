# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num=0
        for nums in operations:
            if nums == "++X" or nums=="X++":
                num+=1
                print("1",num)
            elif nums == "--X" or nums=="X--":
                num-=1
                print("2",num)
        return num
