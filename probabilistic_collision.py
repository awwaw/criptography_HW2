import random
from Utils import Utils


def sub(a: int, b: int, mod: int) -> int:
    return (a - b) % mod


#
#   Based on Collision Theorem
#
def probabilistic_collision(p: int, g: int, a: int, prime: bool = True) -> int:
    n = p - 1 if prime else Utils().find_primitive(p, g)

    first_urn = {}
    second_urn = {}

    while True:
        num = random.randint(1, n)
        first = Utils().pow(g, num, p)
        second = (a * first) % p

        if first in second_urn:
            return sub(num, second_urn[first], n)

        if second in first_urn:
            return sub(first_urn[second], num, n)

        first_urn[first] = num
        second_urn[second] = num
