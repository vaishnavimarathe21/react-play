def knapsack(values, weights, W):
    n = len(values)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    res = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            res.append(i-1)
            w -= weights[i-1]
    res.reverse()
    return dp[n][W], res

def main():
    values = [60,100,120]
    weights = [10,20,30]
    W = 50
    best, items = knapsack(values, weights, W)
    print("Max value", best)
    print("Items chosen indices", items)

if __name__ == "__main__":
    main()
