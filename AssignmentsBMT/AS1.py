import math

def ultimate_greyness(colors):
    n = len(colors)
    min_diff = math.inf  # Start with a large number to track the minimum difference

    # Loop through all subsets (except the empty set)
    for mask in range(1, 1 << n):
        total_vividness = 1  # Product of vividness
        total_dullness = 0   # Sum of dullness

        for i in range(n):
            if mask & (1 << i):  # If the ith color is included in the subset
                total_vividness *= colors[i][0]  # Multiply vividness
                total_dullness += colors[i][1]   # Add dullness

        # Calculate the absolute difference
        diff = abs(total_vividness - total_dullness)
        min_diff = min(min_diff, diff)

    return min_diff

# Input reading
n = int(input())  # Number of colors
colors = []

for _ in range(n):
    v, d = map(int, input().split())  # Vividness and dullness
    colors.append((v, d))

# Output the smallest possible difference
print(ultimate_greyness(colors))
