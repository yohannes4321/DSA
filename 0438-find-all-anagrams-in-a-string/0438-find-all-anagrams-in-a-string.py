class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # LET USE TWO DICTONARY 

        p_dict={}
        s_dict={}
        res=[]
        for i in range(len(p)):
            if p[i] not in p_dict:
                p_dict[p[i]]=1
            else:
                p_dict[p[i]]+=1
        for i in range(len(s)):
            if s[i] not in  s_dict:
                s_dict[s[i]]=1
            elif s[i] in s_dict:
                s_dict[s[i]]+=1
            if i>=len(p):# which means not equell but greater than len(p)
                s_dict[s[i-len(p)]] -=1
                if s_dict[s[i-len(p)]]==0:
                    del s_dict[s[i-len(p)]]
            if p_dict == s_dict:
                res.append(i-len(p)+1)
        return res
