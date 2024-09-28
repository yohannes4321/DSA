class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameandheight={}
        res=[]
        for h ,n in zip(heights,names):
            nameandheight[h]=n
        for h in reversed(sorted(heights)):
            res.append(nameandheight[h])
        return res
   