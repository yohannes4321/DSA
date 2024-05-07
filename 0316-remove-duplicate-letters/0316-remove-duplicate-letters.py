class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = [0] * 26  # Track last index of occurrence for each element
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
        
        stack = []  # Monotonic stack to maintain increasing order of chars
        seen = [False] * 26  # Track already included elements
        for i in range(len(s)):
            if seen[ord(s[i]) - ord('a')]:
                # Don't process already included char
                freq[ord(s[i]) - ord('a')] -= 1
                continue
            while stack and stack[-1] > s[i] and freq[ord(stack[-1]) - ord('a')] > 0:
                # Pop all possible larger chars
                seen[ord(stack[-1]) - ord('a')] = False
                stack.pop()
            stack.append(s[i])
            seen[ord(s[i]) - ord('a')] = True
            freq[ord(s[i]) - ord('a')] -= 1
        
        # Build answer string
        return "".join(stack)