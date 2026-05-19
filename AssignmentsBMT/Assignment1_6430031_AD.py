

def harvester_count(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        memo[n] = harvester_count(n - 1, memo) + harvester_count(n - 2, memo)
        return memo[n]

# Input: generation number
n = int(input("Enter the generation number: "))
print(harvester_count(n))
