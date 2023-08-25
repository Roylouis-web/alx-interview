#!/usr/bin/python3
"""
    Module for a function called makeChange
"""


def makeChange(coins, total):
    """
        Calculates the fewest steps to get a total
    """

    if total <= 0:
        return 0
    if type(total) != int:
        return -1
    if not coins or type(coins) != list:
        return -1
    if any([coin == 0 or type(coin) != int for coin in coins]):
        return -1
    if any([coin == total for coin in coins]):
        return 1
    n = max(coins)
    prev_coins = []
    count = 0

    while total > 0:
        unchecked = list(filter(lambda x: x not in prev_coins, coins))
        if ((total - n) == 0):
            count += 1
            return count
        if (any([(
            (total - n) % coin == 0 and
            (total - n) >= coin and
            total >= n) or
            (((total - n) + 1) % coin == 0 and (total - n) >=
                coin and total >= n) for coin in unchecked
             ])):
            total -= n
            count += 1
        else:
            prev_coins.append(n)
            check = list(filter(lambda x: x not in prev_coins, coins))
            if check:
                n = max(check)
            else:
                return -1
    return count
