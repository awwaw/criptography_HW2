import random
from typing import Callable
from sympy import mod_inverse

from Utils import Utils


def shuffling_function(x: int, g: int, h: int, p: int) -> int:
    if x < p // 3:
        return g * x
    if p // 3 <= x < 2 * p // 3:
        return x ** 2
    if 2 * p // 3 <= x < p:
        return h * x
    else:
        return x


def applyable_shuffle(g: int, h: int, p: int) -> Callable[[int], int]:
    return lambda x: shuffling_function(x, g, h, p)


def shuffle(seq: list, g: int, h: int, p: int) -> list:
    return list(map(applyable_shuffle(g, h, p), seq))


def double_shuffle(seq: list, g: int, h: int, p: int) -> list:
    shuffled = shuffle(seq, g, h, p)
    return shuffle(shuffled, g, h, p)


def update_values(u: int, v: int, x: int, p: int) -> tuple:
    if x < p // 3:
        return (u + 1) % (p - 1), v
    elif x < 2 * p // 3:
        return (2 * u) % (p - 1), (2 * v) % (p - 1)
    else:
        return u % (p - 1), (v + 1) % (p - 1)


def update_list(xs: list, p: int, g: int, h: int) -> list:
    u, v = update_values(*xs, p)
    return [u, v, (pow(g, u, p) * pow(h, v, p)) % p]


def double_update(xs: list, p: int, g: int, h: int) -> list:
    return update_list(update_list(xs, p, h, g), p, g, h)


def get_order(prime: bool, p: int, g: int, h: int) -> int:
    if prime:
        return p - 1
    get_primitive = Utils().find_primitive
    o1 = get_primitive(p, g)
    o2 = get_primitive(p, h)
    return (o1 * o2) // Utils().gcd(o1, o2)


def pollard_rho(p: int, g: int, h: int, prime: bool = False):
    order = get_order(prime, p, g, h)

    xs = [0, 0, 1]
    ys = [0, 0, 1]

    while True:
        xs = update_list(xs, p, g, h)
        ys = double_update(ys, p, g, h)

        if xs[-1] == ys[-1]:
            x0 = xs[0]
            x1 = xs[1]
            y0 = ys[0]
            y1 = ys[0]
            diff1 = (x0 - y0) % order
            diff2 = (x1 - y1) % order
            gc, x, y = Utils().gcdex(diff2, p - 1)
            if gc == 1:
                return diff2 * Utils().inverse(diff1, p - 1)

            x %= order
            diff1 = (x * diff1) % order
            diff2 = gc

            gcd = Utils().gcd
            new_gc = gcd(diff2, gcd(diff1, order))
            new_p = order // new_gc

            diff1 //= new_gc
            diff2 //= new_gc
            diff1 = (diff1 * mod_inverse(diff2, new_p)) % new_p

            for i in range(gc):
                if pow(g, diff1 + i * new_p, p) == h:  # Here I realized that there is builtin pow function
                    return diff1 + i * new_p
            return -1
