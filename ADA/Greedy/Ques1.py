# Coin Change — Minimum Coins
# You are given an amount and a list of coin denominations. Find the minimum number of coins required to make that amount using the Greedy approach.

# Example:
coins = [1, 2, 5, 10]
amount = 18










def coinChange(amount):
    coins = [1, 2, 5, 10]
    count =0
    for coin in coins:
        while amount>= coin:
            amount-=coin
            count+=1

    return count


print(coinChange(18))