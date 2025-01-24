#!/usr/bin/python3
"""
Given a list of coin denominations and a total amount, return the minimum
number of coins needed to make the total amount. If it is not possible to
make the total amount, return -1.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    Args:
        coins (list): List of coin denominations.
        total (int): Target total amount.
    Returns:
        int: Fewest number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to prioritize larger denominations
    coins.sort(reverse=True)
    memo = {}

    def dfs(remaining):
        # Base cases
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')

        # Check memoization
        if remaining in memo:
            return memo[remaining]

        # Explore options using each coin
        min_coins = float('inf')
        for coin in coins:
            num_coins = 1 + dfs(remaining - coin)
            min_coins = min(min_coins, num_coins)

        # Store result in memo and return
        memo[remaining] = min_coins
        return min_coins

    result = dfs(total)
    return result if result != float('inf') else -1
