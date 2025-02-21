# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Initialize a hash table to store the number of losses for each player
        hash_table = {}
        # Initialize an empty list for players with no losses
        res = [[],[]]

        # Iterate through each match
        for w, l in matches:
            # Update the hash table for the winner and loser
            if w not in hash_table:
                hash_table[w] = 0
            hash_table[l] = 1 + hash_table.get(l, 0)

        # Populate the result lists
        for key, value in hash_table.items():
            if value < 2:
                res[value].append(key)

        # Return the lists (sorted in increasing order)
        return [sorted(res[0]), sorted(res[1])]