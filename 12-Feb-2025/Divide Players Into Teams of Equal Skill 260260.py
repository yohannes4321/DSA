# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        left=0
        right=len(skill)-1
        total=0
        sum_value=skill[left]+skill[right]
        while left < right:
            if skill[left]+skill[right]!=sum_value:
                return -1
            else:
                total+=skill[left]*skill[right]
            left+=1
            right-=1
        return total
