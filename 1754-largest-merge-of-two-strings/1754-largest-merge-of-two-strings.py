class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        i, j = 0, 0
        ans = []  # List to store characters for the merge

        while i < len(word1) and j < len(word2):
            # Compare substrings starting from current indices
            if word1[i:] > word2[j:]:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1

        # Append remaining characters from non-empty string
        ans.extend(word1[i:])
        ans.extend(word2[j:])

        return ''.join(ans)
