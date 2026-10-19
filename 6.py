
def matrix_chain(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1] if n > 0 else 0


dimensions = [10, 30, 5, 60]

print("Minimum Multiplications:", matrix_chain(dimensions))
