from collections import deque
import sys

# Define the target configuration
target = "123456780"  

# Define the possible movements
moves = {
    0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
    3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
    6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
}

# Function to swap tiles
def swap(state, i, j):
    lst = list(state)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

# BFS function to solve the puzzle
def bfs(start):
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        state, depth = queue.popleft()
        
        if state == target:
            return depth
        
        zero_index = state.index('0')
        
        for move in moves[zero_index]:
            new_state = swap(state, zero_index, move)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, depth + 1))
    
    return -1  # Return -1 if the puzzle is unsolvable

# Function to check if the puzzle is solvable
def is_solvable(state):
    inversion_count = 0
    state = state.replace('0', '')  # Remove the blank tile for inversion counting
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] > state[j]:
                inversion_count += 1
    return inversion_count % 2 == 0

# Modify input reading to match the judge's expected format
try:
    # Read the input from standard input (this will work with the judge)
    input_data = sys.stdin.read().strip().split()
    
    # Convert the grid into a single string format
    start_state = ''.join(input_data)
    
    # Check if the puzzle is solvable
    if not is_solvable(start_state):
        print("unsolvable")
    else:
        # Solve the puzzle
        result = bfs(start_state)
        if result != -1:
            print(result)
        else:
            print("unsolvable")

except Exception as e:
    print(f"Runtime error: {e}", file=sys.stderr)
