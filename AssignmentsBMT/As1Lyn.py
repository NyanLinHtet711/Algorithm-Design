from itertools import combinations

def calculate_difference(colors):
    total_v = 1
    total_d = 0
    for color in colors:
        v, d = color
        total_v *= v
        total_d += d
        # print(abs(total_v - total_d))
    return abs(total_v - total_d)


def find_smallest_difference():
    N = int(input())
    min_diff = float('inf')
    colors = []

    for _ in range(N):
        v, d = map(int, input().split())
        colors.append((v, d))

    for size in range(1, N + 1):
        for combination in combinations(colors, size):
            # print(combination)
            diff = calculate_difference(combination)
            min_diff = min(min_diff, diff)

    print(min_diff)


find_smallest_difference()