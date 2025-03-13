# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            decoded = ""   
            num = 0  
            while index < len(s):
                char = s[index]

                if char.isdigit():   
                    num = num * 10 + int(char)

                elif char == '[':   
                    index, nested_string = helper(index + 1)   
                    decoded += num * nested_string   
                    num = 0   

                elif char == ']':   
                    return index, decoded   

                else:   
                    decoded += char

                index += 1   

            return decoded 

        return helper(0)   
