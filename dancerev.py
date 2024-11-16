def calculate_min_moves(num_instructions, dance_steps):
    # Mapping tiles to indices for easier access
    tiles = ['up', 'down', 'left', 'right']
    tile_to_index = {tile: idx for idx, tile in enumerate(tiles)}

    # Number of tiles
    total_tiles = len(tiles)

    # Infinite value for comparison
    MAX_COST = float('inf')

    # Create a DP table initialized with infinity
    dp = [[[MAX_COST] * total_tiles for _ in range(total_tiles)] for _ in range(num_instructions + 1)]

    # Initial state: legs can start on any two distinct tiles with zero cost
    for first_leg in range(total_tiles):
        for second_leg in range(total_tiles):
            if first_leg != second_leg:
                dp[0][first_leg][second_leg] = 0

    # Fill the DP table based on instructions
    for step in range(1, num_instructions + 1):
        target_tile = tile_to_index[dance_steps[step - 1]]
        for leg1 in range(total_tiles):
            for leg2 in range(total_tiles):
                if leg1 == leg2:
                    continue
                # Option 1: Move leg1 to the target tile
                dp[step][target_tile][leg2] = min(
                    dp[step][target_tile][leg2],
                    dp[step - 1][leg1][leg2] + (0 if leg1 == target_tile else 1)
                )
                # Option 2: Move leg2 to the target tile
                dp[step][leg1][target_tile] = min(
                    dp[step][leg1][target_tile],
                    dp[step - 1][leg1][leg2] + (0 if leg2 == target_tile else 1)
                )

    # Find the smallest cost after processing all steps
    minimum_moves = MAX_COST
    for leg1 in range(total_tiles):
        for leg2 in range(total_tiles):
            if leg1 != leg2:
                minimum_moves = min(minimum_moves, dp[num_instructions][leg1][leg2])

    return minimum_moves


# Example usage
instructions_count1 = 6
instructions1 = ["down", "right", "down", "up", "right", "down"]
print(calculate_min_moves(instructions_count1, instructions1))  # Output: 2

instructions_count2 = 8
instructions2 = ["up", "right", "down", "up", "up", "down", "right", "left"]
print(calculate_min_moves(instructions_count2, instructions2))  # Output: 3
