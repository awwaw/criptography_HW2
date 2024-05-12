from Utils import Utils
import math


#
#   Based on algorithm described here: https://en.wikipedia.org/wiki/Baby-step_giant-step
#
def babystep_giantstep(p: int, g: int, a: int, prime: bool = False):
    utils = Utils()
    n = p - 1 if prime else utils.find_primitive(p, g)
    tmp = int(math.sqrt(n)) + 1
    values = {1: 0}
    idx = 1

    for i in range(1, tmp + 1):
        print(f"i - {i}, tmp - {n}")
        idx = (idx * g) % p
        values[idx] = i
    inversed = utils.inverse(utils.pow(g, tmp, p), p)
    idx = a

    for i in range(n + 1):
        print(f"i - {i}, n - {n}, values.size() - {len(values)}")
        if idx in values:
            return i * n + values[idx]
        idx = (idx * inversed) % p
    return -1
