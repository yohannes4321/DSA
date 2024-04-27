class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_value=set()
        left=0
        max_length=0
        for right in range (len(s)):
            while s[right] in set_value:
                set_value.remove(s[left])
                left+=1
            set_value.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length