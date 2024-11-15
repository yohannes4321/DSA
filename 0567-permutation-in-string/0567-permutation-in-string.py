class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Lengths of strings
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, s2 cannot contain a permutation of s1
        if len1 > len2:
            return False
        
        # Create frequency arrays for s1 and the initial window in s2
        s1_freq = [0] * 26
        window_freq = [0] * 26
        
        # Fill frequency arrays for s1 and the first window of s2
        for i in range(len1):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1
        
        # Check initial window
        if s1_freq == window_freq:
            return True
        
        # Sliding window over the rest of s2
        for i in range(len1, len2):
            # Add new character to the window
            window_freq[ord(s2[i]) - ord('a')] += 1
            # Remove the character that is no longer in the window
            window_freq[ord(s2[i - len1]) - ord('a')] -= 1
            
            # Check if the window matches the s1 frequency
            if s1_freq == window_freq:
                return True
        
        return False
