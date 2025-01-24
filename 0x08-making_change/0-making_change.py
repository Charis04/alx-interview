#!/usr/bin/env python3
"""
Given a list of coin denominations and a total amount, return the minimum
number of coins needed to make the total amount. If it is not possible to
make the total amount, return -1.
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make a given amount of
    change.
    Args:
        coins (list): A list of the values of the available coins.
        total (int): The total amount of change needed.
    Returns:
        int: The minimum number of coins needed to make the change, or -1 if
        it is not possible.
    """
    if total <= 0:
        return 0

    # Initialize the array to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
