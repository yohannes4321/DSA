class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_maps=set()
        max_length=0
        left=0
        for right in range(len(s)):
            
            while s[right] in hash_maps:
                 
                    
                hash_maps.remove(s[left])
                left+=1
            hash_maps.add(s[right])
            max_length=max(max_length,right-left+1)
        return max_length


            

            
