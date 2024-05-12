from pollard_rho_algorithm import pollard_rho
from probabilistic_collision import probabilistic_collision
from steps import babystep_giantstep
from typing import Callable
import random
import time


def brute_force(p: int, g: int, a: int, prime: bool = False) -> int:
    tmp_pow = 1
    for i in range(p):
        tmp_pow = (tmp_pow * g) % p
        if tmp_pow == a:
            return i + 1
    return -1


class TestingFunction:
    def __init__(self, name: str, method: Callable):
        self.name = name
        self.method = method

    def get_name(self) -> str:
        return self.name

    def get_method(self) -> Callable:
        return self.method


def test(method: TestingFunction, primes_amount: int, modulo: int, root: int) -> None:
    primes = [random.randint(1, modulo) for _ in range(primes_amount)]
    print(f"Testing {method.get_name()}")
    function = method.get_method()
    start = time.time()
    for idx, h in enumerate(primes):
        if (idx + 1) % 10 == 0 or idx + 1 == len(primes):
            print(f"Done - {idx + 1}")
        try:
            result = function(modulo, root, h, True)
            if (root ** result) % modulo != h:
                print(f"ERROR: result {result} is not correct! {root}^{result} % {modulo} is not equal to {h}")
        except Exception as e:
            print(f"An error occurred while trying to calculate result - {e}")
    total_time = time.time() - start
    print(f"{primes_amount} runs completed in {total_time}, " +
          f"with average run time equal to {total_time / primes_amount}")


def test_all(primes_amount: int, modulo: int, root: int) -> None:
    methods = [
        # TestingFunction("BruteForce", brute_force),
        # TestingFunction("BabyStep-GiantStep", babystep_giantstep),
        # TestingFunction("Probabilistic Collision Algorithm", probabilistic_collision),
        TestingFunction("Pollard's Rho Algorithm", pollard_rho)
    ]
    for method in methods:
        test(method, primes_amount, modulo, root)


def main():
    test_cases = [
        [100, 1000003, 7],
        [10, 9999991, 22],
        [1, 1000000007, 13]
    ]

    for primes_amount, modulo, root in test_cases:
        print(f"Now testing with parameters:")
        print(f"Amount of primes - {primes_amount}")
        print(f"Modulo - {modulo}")
        print(f"Root - {root}")

        test_all(primes_amount, modulo, root)

        print("------------------------")


if __name__ == "__main__":
    main()
