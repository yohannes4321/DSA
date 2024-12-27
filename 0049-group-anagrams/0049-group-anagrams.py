class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
         
        dictonary={}
        for word in strs:
            list_value=[0]*26
            for i in word:
                list_value[ord(i)-ord("a")]+=1
            if tuple(list_value) in dictonary :
                dictonary[tuple(list_value)].append(word)
            else:
                 
                dictonary[tuple(list_value)]=[word]
        return dictonary.values()
        