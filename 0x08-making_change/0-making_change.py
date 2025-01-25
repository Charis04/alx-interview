#!/usr/bin/python3
"""
Given a list of coin denominations and a total amount, return the minimum
number of coins needed to make the total amount. If it is not possible to
make the total amount, return -1.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target amount to be reached.

    Returns:
        int: The minimum number of coins needed to meet the total,
             or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    for coin in coins:
        if total == 0:
            break
        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin

    return count if total == 0 else -1
