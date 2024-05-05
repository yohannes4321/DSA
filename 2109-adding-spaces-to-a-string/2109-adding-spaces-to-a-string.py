class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
    
        modified_chars = []  # List to store modified characters
        space_idx = 0  # Index for the spaces list

        for i, char in enumerate(s):
            if space_idx < len(spaces) and i == spaces[space_idx]:
                modified_chars.append(' ')  # Add a space before the character
                space_idx += 1
            modified_chars.append(char)  # Add the character

        return ''.join(modified_chars)