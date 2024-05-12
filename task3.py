import math
from sympy import sqrt_mod
from Utils import Utils
import random


def solve_linear_equation(matrix: list[list]) -> list[list]:
    matrix = Utils().transpose(matrix)
    matrix = [
        list(map(lambda x: x % 2, row))
        for row in matrix
    ]

    i = 0
    solved = set()
    seq = []
    for i1 in range(len(matrix[0])):
        found = False
        for j in range(i, len(matrix)):
            if matrix[j][i1]:
                matrix[i], matrix[j] = matrix[j], matrix[i]
                found = True
                break
        if not found:
            continue

        j = 0
        while j < len(matrix):
            if matrix[j][i1]:
                matrix[j] = Utils().sub(matrix[j], matrix[i]).copy()
            j += 1
            if j == i:
                continue

        seq.append(i1)
        solved.add(i1)
        i += 1

    ans = []
    for i in range(len(matrix[0])):
        if i in solved:
            continue

        tmp = [0 if _ != i else 1 for _ in range(len(matrix[0]))]

        for j in range(len(seq)):
            if matrix[j][i]:
                tmp[seq[j]] = 1
        ans.append(tmp)
    return ans


def quadratic_sieve_factor(n: int) -> int:
    a = 1_000_000
    square = round(math.sqrt(n))

    t = [(square + i) ** 2 - n for i in range(0, a + 1)]
    primes = [prime for prime in Utils().eratosthenes(5_000) if Utils().pow(n, prime // 2, prime) == 1]
    divisors = [[0 for _ in range(len(primes))] for __ in range(len(t))]

    for j in range(len(primes)):
        prime = primes[j]
        num = prime
        while num < t[-1]:
            roots = sqrt_mod(n, num, True)
            if len(roots) == 0:
                break

            for root in roots:
                root = (root - square) % num
                for i in range(root, len(t), num):
                    t[i] //= prime
                    divisors[i][j] += 1
            num *= prime

    s = []
    matrix = []

    for i in range(len(t)):
        if t[i] != 1:
            continue
        s.append(i + square)
        matrix.append(divisors[i])

    solved = solve_linear_equation(matrix)
    for row in solved:
        n1 = 1
        n2 = [0 for _ in range(len(primes))]
        for j in range(len(row)):
            if row[j] == 1:
                n1 *= s[j]
                for k in range(len(matrix[0])):
                    n2[k] += matrix[j][k]

        res = 1
        for j in range(len(n2)):
            res *= primes[j] ** (n2[j // 2])

        divisor = Utils().gcd(n, (n1 - res) % n)
        if divisor != 1 and divisor != n:
            return divisor
    return -1


def main() -> None:
    for i in range(5):
        n = random.randint(10**8, 10**13)
        print(f"n is - {n}")
        print(f"Non-trivial divisor of {n} is - {quadratic_sieve_factor(n)}")


if __name__ == "__main__":
    main()
