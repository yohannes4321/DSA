class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        #  this is greedy algorthim 
        if k<= numOnes:
            return k
        elif k<= numOnes+numZeros:
            return numOnes
        else:
            return numOnes +( (k -(numOnes+numZeros))*-1)