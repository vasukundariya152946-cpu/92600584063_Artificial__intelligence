# 3. Implement Depth First Search (for 8 puzzle problem).
# Name:- Kundariya Vasu 
# Enrollment No :- 92600584063


goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Function to print the puzzle
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Generate possible moves
# Order: Up -> Down -> Left -> Right
def get_neighbors(state):

    neighbors = []

    # Find position of blank (0)
    zero = state.index(0)

    # Convert position into row and column
    row, col = divmod(zero, 3)

    # Possible movements
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    # Generate all possible states
    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check valid position
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            # Find new position of blank
            new_zero = new_row * 3 + new_col

            # Convert tuple to list
            new_state = list(state)

            # Swap blank with new position
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            # Convert list back to tuple
            neighbors.append(tuple(new_state))

    return neighbors


# DFS function
def dfs(start):

    # Stack contains:
    # (current_state, path)
    stack = [(start, [])]

    # Store visited states
    visited = {start}

    while stack:

        # Remove last element (DFS)
        state, path = stack.pop()

        # Check goal
        if state == goal:
            return path + [state]

        # Generate neighbors
        neighbors = get_neighbors(state)

        # Reverse order to maintain
        # Up -> Down -> Left -> Right
        for next_state in reversed(neighbors):

            # Check if already visited
            if next_state not in visited:

                visited.add(next_state)

                # Add to stack
                stack.append(
                    (next_state, path + [state])
                )

    return None


# Starting state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)


# Run DFS
solution = dfs(start)


# Print solution
if solution:

    print("Solution found in",
          len(solution) - 1,
          "moves:\n")

    for step in solution:
        print_board(step)

else:

    print("No solution found.")
# solution = dfs (start)
# if solution:
#     print("solutin found in",len(solution)-1,"moves:\n")
#     for step in solution:
#         print_board(step)
# else:
#     print("no solution found.")
                 
    
