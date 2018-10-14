class Solution:

    def countPrimes_slow(self, num):
        """
        :type n: int
        :rtype: int
        """
        if num <= 2:
            return 0
        primes = []
        for i in range(3, num, 2):
            is_prime = True
            for prime in primes:
                if i % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
        return len([2] + primes)

    def countPrimes(self, num):
        """ https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes """
        if num <= 2:
            return 0
        nums = [1] * (num)
        nums[0] = 0
        nums[1] = 0
        for idx in range(2, num):
            if nums[idx] == 1:
                for idx2 in range(idx*idx, num, idx):
                    nums[idx2] = 0
        return sum(nums)
