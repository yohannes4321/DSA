class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        left = 0
        hash_mapp = {}
        hash_maps = {}
        if len(s)<len(p):
            return []
        # Initialize hash_mapp with frequency counts for pattern p
        for right in range(len(p)):
            hash_mapp[p[right]] = 1 + hash_mapp.get(p[right], 0)

            hash_maps[s[right]] = 1 + hash_maps.get(s[right], 0)

        # Check if the first window is an anagram
        if hash_mapp == hash_maps:
            res.append(left)

        # Slide the window over s
        for right in range(len(p), len(s)):
            # Update hash_maps for the new character at the right end
            hash_maps[s[right]] = 1 + hash_maps.get(s[right], 0)
            # Decrease hash_maps for the character at the left end
            hash_maps[s[left]] -= 1
            if hash_maps[s[left]] == 0:
                del hash_maps[s[left]]
            left += 1

            # Check if the current window is an anagram
            if hash_mapp == hash_maps:
                res.append(left)

        return res
