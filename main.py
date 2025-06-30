from itertools import combinations
from math import gcd
from random import randint


def break_rsa_from_d(n: int, e: int, d: int):
    k = d*e - 1

    while True:
        g = random.randint(1, n - 1)
        # This is just a mathematical check
        # The chance for this to happen is roughly 2*sqrt(n)/n. Negligible for n >= 1024.
        if (gcd(g, n)) != 1:
            p = gcd(g, n)
            return p, n // p

        # g**k must always be 1
        # assert pow(g, k, n) == 1
        
        f = 1
        while k % 2**(f+2) == 0 and pow(g, k // 2**(f + 1), n) == 1:
            f += 1

        m = k // (2**f)

        root = pow(g, m // 2, n)

        # From the construction, root is  a square root of 1.
        # In Z_n, for n = p * q, the square root of 1 has 4 different solutions
        # Two of the solutions are 1 and -1. The other two are called non-trivial solutions.
        # We wan't to find a non-trivial square root of 1.

        if root != n - 1 and root != 1:
            p = gcd(n, root - 1)
            # assert p > 1
            return p, n // p


def main():
    p = 29619082031781708758789445286032309089689245581404437540274962433
    q = 36201100261066532927409322016261711109620189043938756993669398529
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 13
    d = pow(e, -1, phi)

    print(break_rsa_from_d(n, e, d))


if __name__ == "__main__":
    main()
