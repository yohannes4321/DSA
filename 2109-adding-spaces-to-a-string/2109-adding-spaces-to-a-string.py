class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
    
        modeifed_c =[]
        space_index=0
        for i in range(len(s)):
            if space_index < len(spaces) and i == spaces[space_index]:
                modeifed_c.append(" ")
                space_index +=1
            modeifed_c.append(s[i])
        return "".join(modeifed_c)