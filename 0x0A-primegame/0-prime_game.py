#!/usr/bin/python3
"""
Determine the winner of each game.
"""

def isWinner(x, nums):
    """
    Determine the winner of each game.

    :param x: int, number of rounds
    :param nums: List[int], array of n values for each round
    :return: str, name of the player with the most wins or None if it's a tie
    """
    def sieve_of_eratosthenes(n):
        """
        Generate a list of primes up to n using the Sieve of Eratosthenes.
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False
        return [i for i in range(n + 1) if is_prime[i]]

    def count_prime_moves(n):
        """Count the number of prime moves possible for a given n."""
        primes = sieve_of_eratosthenes(n)
        moves = 0
        marked = set()
        for prime in primes:
            if prime not in marked:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    marked.add(multiple)
        return moves

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1  # No primes, Ben wins by default
            continue

        moves = count_prime_moves(n)
        if moves % 2 == 0:
            ben_wins += 1  # Ben wins if moves are even
        else:
            maria_wins += 1  # Maria wins if moves are odd

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
