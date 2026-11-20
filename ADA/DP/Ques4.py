def minCostClimbingStairs(cost):

    dp = [0 , 1]
    costs = []
    for i in range(2 , len(cost)-1):
        costs.append(min((dp[i-2],cost[i-2]) ,(dp[i-1],cost[i-1]) ))
        
    return dp , min(costs)
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))