class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        hash_set=set(arr2)
        end=[]
        dictonary={}
        for i in arr1:
            if i not in hash_set:
                end.append(i)

            if i in dictonary :
                dictonary[i]+=1
            elif i not in dictonary:
                dictonary[i]=1
        end.sort()
        res=[]
        # the outside is array2 and inside the array 1
        for i in arr2 :
            print(dictonary)
            for _ in range(dictonary[i]):
                res.append(i)
        res=res+end
        return res 
        