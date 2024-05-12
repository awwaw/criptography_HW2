class Utils:
    def __init__(self):
        pass

    def gcd(self, a: int, b: int):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def pow(self, x, p, m):
        if p == 0:
            return 1
        if p % 2 == 1:
            return (self.pow((x * x) % m, p // 2, m) * x) % m
        return self.pow((x * x) % m, p // 2, m)

    def sub(self, a: list, b: list) -> list:
        if len(a) != len(b):
            raise RuntimeError("Lists must have equal lengths")
        return [(a[i] - b[i]) % 2 for i in range(len(a))]

    def transpose(self, matrix: list[list]) -> list[list]:
        ans = []
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            ans.append(row)
        return ans

    def eratosthenes(self, n: int) -> list:
        prime = [True for _ in range(n + 1)]
        primes = []

        for p in range(2, n + 1):
            if prime[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    prime[i] = False
        return primes

    def gcdex(self, a: int, b: int) -> tuple:
        x0, x1 = 1, 0
        y0, y1 = 0, 1

        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0

    def inverse(self, x: int, p: int):
        return self.pow(x, p - 2, p)

    def find_all_divisors(self, n: int) -> list:
        i = 1
        res = []
        while i * i <= n:
            if i * i == n:
                res.append(i)
            else:
                if n % i == 0:
                    res.append(n // i)
                    res.append(i)
            i += 1
        return sorted(res)

    def find_primitive(self, p, g):
        divs = self.find_all_divisors(p - 1)
        prev = 0
        s = 1
        for i in divs:
            diff = pow(g, i - prev, p)
            s = (s * diff) % p
            if s == 1:
                return i
            prev = i
        return p - 1