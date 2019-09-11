class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # All numbers start as prime
        is_prime = [True] * n

        # Sieve of Erathanos
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # Now count primes
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                
        return count