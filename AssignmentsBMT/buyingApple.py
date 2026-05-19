def minimum_cost_to_buy_apples(n, k, prices):
    dp = [float('inf')] * (k + 1)
    dp[0] = 0  
    
    for i in range(1, k + 1):
        for j in range(k):
            if j < len(prices) and prices[j] != -1 and i >= j + 1:
                dp[i] = min(dp[i], dp[i - (j + 1)] + prices[j])
    
    return dp[k] if dp[k] != float('inf') else -1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        prices = list(map(int, data[index:index + k]))
        index += k
        result = minimum_cost_to_buy_apples(n, k, prices)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
