# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
         
        mydict={}
        for i in range(len(list1)):
            if list1[i] in list2:
                mydict[list1[i]]=i+list2.index(list1[i])
        mydict=sorted(mydict.items(),key=lambda x:x[1])
        print(mydict)
        l=[]
        z=mydict[0][1]
        for i in range(len(mydict)):
            if mydict[i][1]==z:
                l.append(mydict[i][0])
            else:
                break
        return l
        
        
        
            



 
        
