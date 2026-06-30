def countTilingPatterns(L):
    if L == 0:
        return 1
    elif L == 2:
        return 3
    
    MOD = 44711
    f = [0] * (L + 1)
    f[0] = 1
    f[2] = 3

    for i in range(4, L + 1, 2):
        f[i] = (4 * f[i - 2] - f[i - 4]) % MOD

    return f[L]

# Example usage
input_lengths = list(map(int, input().split()))

for L in input_lengths:
    result = countTilingPatterns(L)
    print("Input:", L, "Output:", result)

