class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        for i in range(rowIndex):
            newres=[0]*(len(res)+1)
            for j in range(len(res)):
                newres[j]+=res[j]
                newres[j+1]+=res[j]
            res=newres
        return res
            