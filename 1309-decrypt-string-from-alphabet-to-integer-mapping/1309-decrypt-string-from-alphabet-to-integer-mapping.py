class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i+2])  # Extract the number
                res.append(alphabet[num - 1])  # Append the corresponding character
                i += 3  # Skip the '#'
            else:
                num = int(s[i])
                res.append(alphabet[num - 1])
                i += 1
        return ''.join(res)  # Convert the list of characters to a string
 