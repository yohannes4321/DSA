# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            decoded = ""  # This stores the decoded part of the string
            num = 0  # This stores the repetition number

            while index < len(s):
                char = s[index]

                if char.isdigit():  # If it's a number, build the full number
                    num = num * 10 + int(char)

                elif char == '[':  # Start decoding nested part
                    index, nested_string = helper(index + 1)  # Call recursion
                    decoded += num * nested_string  # Repeat the decoded part
                    num = 0  # Reset number

                elif char == ']':  # End of a nested part
                    return index, decoded  # Return to the previous level

                else:  # Normal character, add it directly
                    decoded += char

                index += 1  # Move to the next character

            return decoded  # Return the final decoded string

        return helper(0)  # Start from index 0
