def fib(n):
    if n <= 1:
        return n

    dp = [0, 1]
    for i in range(2 , n+1):
        if i not in dp:
            dp.append(dp[i-1]+ dp[i-2])

    # Complete the loop here

    return dp[n]

print(fib(6))