"""Project Euler #203: Squarefree Binomial Coefficients
"""

from collections import defaultdict


class SquarefreeBinomialCoefficients:

    def __init__(self, rows):
        self.rows = rows
        self.coefficients = set()  # Unique, squarefree numbers
        self._factorials = {}  # Cache for factorial numbers
        self._primes = set()  # Cache for prime numbers
        self._non_primes = set()  # Cache for non-prime numbers
        self._cache_combinatorial = defaultdict(tuple)  # Cache for nCm

    def add(self, coefficient):
        self.coefficients.add(coefficient)

    def add_from_list(self, lst):
        for coefficient in lst:
            self.add(coefficient)

    def factorial(self, number):
        if number <= 1:
            return 1
        if number in self._factorials:
            return self._factorials[number]
        value = number * self.factorial(number - 1)
        self._factorials[number] = value
        return value

    def combinatorial(self, n, m):
        if self._cache_combinatorial[(n, m)]:
            return self._cache_combinatorial[(n, m)]
        value = self.factorial(n) // (self.factorial(m) * self.factorial(n - m))
        self._cache_combinatorial[(n, m)] = value
        return value

    def get_diagonals(self, skip_first=True):
        j = 1
        mid_point = self.rows // 2
        starts_at = 1 if skip_first else 0
        for i in range(1, self.rows + 1):
            lst = [self.combinatorial(x + i - 1, i - 1) for x in range(starts_at, j)]
            if i > mid_point and self.rows % 2 != 0:
                j -= 1
            elif i == mid_point and self.rows % 2 == 0:
                pass
            elif i > mid_point and self.rows % 2 == 0:
                j -= 1
            else:
                j += 1
            yield lst

    def squarefree(self, diagonals):
        sqrfree = set()
        lst_sqrfree = list(filter(lambda x: self.is_squarefree(x), diagonals))
        for number in lst_sqrfree:
            sqrfree.add(number)
            self.coefficients.add(number)
        return sqrfree

    def is_squarefree(self, n):
        for prime in self.get_primes(n):
            prime_square = prime ** 2
            if prime_square > n:
                break
            if n % prime_square == 0:
                return False
        return True

    def get_primes(self, number):
        # TODO: See if the range can be decreased (We only need prime**2)
        if number <= 1:
            return {}
        # Calculate primes until `number` if we havent already
        if not (number in self._primes or number in self._non_primes):
            for i in range(2, number + 1):
                self.is_prime(i)
        return self._primes

    def is_prime(self, number):
        if number <= 1:
            return False
        if number in self._primes:
            return True
        if number in self._non_primes:
            return False
        for i in range(2, number):
            if number % i == 0:
                self._non_primes.add(number)
                return False
        self._primes.add(number)
        return True

    def squarefree_sum(self):
        sq = {1,}  # 1 is not included in get_diagonals by default
        for diagonal in self.get_diagonals():
            sq = sq.union(self.squarefree(diagonal))
        return sum(sq) % int(10E9 + 7)


if __name__ == '__main__':
    print(SquarefreeBinomialCoefficients(20).squarefree_sum())
