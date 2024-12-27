class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # this is dynamic sliding window 
        left =0
        hashset=set()
        max_length=0
        for right in range(len(s)):
            
            while  s[right ] in hashset:
                hashset.remove(s[left])
                left+=1
            hashset.add(s[right])
            max_length=max(max_length,right-left +1)
        return max_length
            


            