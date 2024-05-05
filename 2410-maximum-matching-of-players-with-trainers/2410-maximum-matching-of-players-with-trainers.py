class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()  # Sort the players by ability
        trainers.sort()  # Sort the trainers by training capacity
        
        match_count = 0  # To keep track of the number of matchings
        p_ptr, t_ptr = 0, 0  # Pointers to iterate through players and trainers
        
        while p_ptr < len(players) and t_ptr < len(trainers):
            # If the player's ability is less than or equal to the trainer's training capacity
            if players[p_ptr] <= trainers[t_ptr]:
                match_count += 1  # Increment the match count
                p_ptr += 1  # Move to the next player
                t_ptr += 1  # Move to the next trainer
            else:
                t_ptr += 1  # Move to the next trainer, as this trainer can't match the current player
        
        return match_count