class Solution:
    # #Solution 1:
    # def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    #         # All possible moves for a knight
    #     moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
    #     def dfs(x, y, steps):
    #         # Base case: If the knight is out of the board, return 0 (probability 0)
    #         if x < 0 or y < 0 or x >= n or y >= n:
    #             return 0
    #         # If no more moves left, return 1 (probability 1)
    #         if steps == 0:
    #             return 1
            
    #         # Initialize probability to 0
    #         prob = 0
            
    #         # Iterate through all possible moves
    #         for dx, dy in moves:
    #             # Calculate the next position after the move
    #             nx, ny = x + dx, y + dy
    #             # Recursively calculate the probability for the next step
    #             prob += dfs(nx, ny, steps - 1) / 8.0
        
    #         return prob
    #     # Call the recursive function starting from the given position and steps
    #     probability = dfs(row, column, k)
    #     return probability
    #Solution 2:
    def knight_probability(n, k, row, column):
    # All possible moves for a knight
        moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
    
    # Create a 3D memoization table to store previously calculated probabilities
        memo = [[[-1 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
    
    # Recursive function with memoization to calculate the probability
        def dfs(x, y, steps):
            # Base case: If the knight is out of the board, return 0 (probability 0)
            if x < 0 or y < 0 or x >= n or y >= n:
                return 0
            # If no more moves left, return 1 (probability 1)
            if steps == 0:
                return 1
            # If the probability for this position and steps is already calculated, return it
            if memo[x][y][steps] != -1:
                return memo[x][y][steps]
            
            # Initialize probability to 0
            prob = 0
            
            # Iterate through all possible moves
            for dx, dy in moves:
                # Calculate the next position after the move
                nx, ny = x + dx, y + dy
                # Recursively calculate the probability for the next step
                prob += dfs(nx, ny, steps - 1) / 8.0
            
            # Store the calculated probability in the memoization table
            memo[x][y][steps] = prob
            return prob
    
        # Call the recursive function starting from the given position and steps
        probability = dfs(row, column, k)
        return probability