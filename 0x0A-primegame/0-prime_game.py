#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Returns a list of primes up to n using Sieve of Eratosthenes"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

def isWinner(x, nums):
    """Determines the winner of the prime game"""
    if x < 1 or not nums:
        return None

    # Get the maximum number in nums for prime precomputation
    max_n = max(nums)
    
    # Precompute primes up to the largest number in nums
    primes_up_to_max = sieve_of_eratosthenes(max_n)
    
    # A list to keep track of how many primes are removable for each n
    prime_count = [0] * (max_n + 1)
    
    # Fill prime_count array with the number of primes up to each number n
    for i in range(2, max_n + 1):
        prime_count[i] = prime_count[i - 1]
        if i in primes_up_to_max:
            prime_count[i] += 1
    
    # Initialize Maria and Ben's win count
    maria_wins = 0
    ben_wins = 0
    
    # For each round, determine the winner
    for n in nums:
        # Maria wins if the number of primes up to n is odd, else Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
