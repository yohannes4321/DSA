class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map={}
        max_length=0
        max_frequancy=0
        left=0
        
        for right in range(len(s)):
            if s[right] not in hash_map:
                hash_map[s[right]]=1
            else:
                hash_map[s[right]]+=1
            max_frequancy=max(max_frequancy,hash_map[s[right]])
            while right-left+1 -max_frequancy>k:#valid
                hash_map[s[left]]-=1
                if  hash_map[s[left]]==0:
                    del  hash_map[s[left]]
                left +=1
            max_length=max(max_length,right-left+1)  
        return max_length
