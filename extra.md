These are some extra notes on things that experimented with, while I was studying the RSA problem.
It turned out I didn't need these proofs, so I didn't include them in the main article. They're also not properly formatted


# The solutions of x^m - a = 0 (mod p)

If p is prime, then x^m - a = 0 has gcd(m, p - 1) distinct solutions.

Let p = 7, m = 5, and a = 1.

All operations modulo 7:
0^5 = 0
1^5 = 1
2^5 = 4
3^5 = 5
4^5 = 2
5^5 = 3
6^5 = 6

Let g be a generator of the prime group.
Express a and x according to the generator: a = g^b, x = g^y.
(g^y)^m = g^b (mod p)
ym = b (mod p-1)

If gcd(m, p-1) = 1, m is invertible, and y = b * m^-1 (mod p-1)

Otherwise, let d = gcd(m, p-1). Let m = k1 * d, and p-1 = k2 * d. Then, gcd(k1, k2) = 1, and gcd(m, k2) = 1.

y*m = c*(p-1) + b, for some integer c

y * m = c * k2 * d + b
y * m = b (mod k2)

Now, gcd(m, k2) = 1. Then, y = b * m^-1 (mod k2).

Taking the initial equation modulo d:

ym = b (mod d)
But m = k1 * d ==> ym = y * k1 * d = 0 (mod d) and b = 0 (mod d).

So, for the equation to satisfy, d must divide b.

Apart from that, the equation doesn't give any information about y. In fact,
y can be anything, and the equation modulo d would still hold.

Then, we can choose y = z (mod d), wlog.

Then, with CRT:
y = b * m^-1 (mod k2)
y = z (mod d)

We can uniquely determine y mod d * k2, where d * k2 = p - 1.

However, there are d choices for z. So, y will have d solutions.

If gcd(m, p - 1) divides b, then the number of solutions for x^m - a = 0 (mod p) is gcd(m, p - 1).

---

# The number a is an mth power residue modulo p, if and only if a^(phi(p)/gcd(m, phi(p))) = 1 (mod p)

Reference: Ireland & Rosen 4.2.1

We will express the elements using a generator of `Z_p*`. Let g be such a generator. We remind its properties:
   - The order of g is p-1 i.e. the equation g^m = 1 (mod p) has m = phi(p) the smallest non-zero solution.
   - Any element in the group can be expressed as g^x, for x in [0, phi(p)].
   - If g^x = g^y (mod p)  ==> x = y (mod phi(p))


## Right to left: a being an mth power residue implies a^(phi(p)/gcd(m, phi(p))) = 1 (mod p) 

Let `d = gcd(m, phi(p))`. Let m = k * d, for some integer k.

If a is an mth power residue:
```
x^m = a (mod p)
```
Then:
```
a^(phi(p)/gcd(m, phi(p))) = a^(phi(p)/d) = (x^m)^(phi(p)/d) = x^(m*phi(p)/d) = x^(k*d*phi(p)/d) = x^(k*phi(p)) = 1 (mod p)
```

## Left to right: if a^(phi(p)/gcd(m, phi(p))) = 1 (mod p), then a is an mth power residue

Let `d = gcd(m, phi(p))` and m = k * d for some integer k. We know that gcd(k, phi(p)) = 1. Otherwise, d could be bigger.

Let g be a generator of `Z_p*`.

Let `g^b = a (mod p)`.

Then, the equation:
```
a^(phi(p)/d) = 1 (mod p)
```
Implies:
```
g^(b*phi(p)/d) = g^0 (mod p)
b*phi(p)/d = 0 (mod phi(p))
```

Meaning that phi(p) divides `b*phi(p)/d`. This means that b/d is an integer,
so d divides b.
```
b = c * d, for some integer c. However, c might not be unique.
```
Then:
```
a = g^b = (g^c)^d (mod p)
```

From before, we know that h^k = g^c (mod p) and gcd(m, phi(p)) divides c, then h has gcd(k, phi(p)) distinct solutions.

Since gcd(m, phi(p)) = 1, h can be uniquely determined from g, c, and k.
Now we can rewrite a:
```
a = (g^c)^d = (h^k)^d = h^(k*d) = h^m (mod p)
```
Which shows that h is the mth root of a. Then, a is an mth power residue.

---

# If g is a quadtratic residue modulo p, then, in can't be a generator, for p > 2

For g to be a generator, the smallest non-zero m such that g^m = 1 (mod p) should be p - 1.

If g is a quadratic residue, then x^2 = g (mod p).

But then (applying Euler's theorem):
    g^((p-1) / 2) = (x^2)^((p-1) / 2) = x^(p-1) = 1 (mod p)

But (p-1) / 2 < p - 1. So g can't be a generator.

---

# If g is an dth power residue modulo p, for a divisor d > 1 of phi(p), g can't be a generator, for p > 2

This is identical to the proof for quadtratic residues. This is a generalization.

Assume g is a generator. Then, the smallest non-zero m for g^m = 1 (mod p) is m = phi(p).

If g is a dth power residue, then:
```
g^(phi(p) / gcd(d, phi(p))) = g^(phi(p)/d) = 1 (mod p)
```

If d > 1, then phi(p) / d  < phi(p), which contradicts with g being a generator.

---

# If, for any divisor d > 1 of phi(p), h is not a dth power residue mod p, then h is a generator, for p > 2

For h to be a generator, h^m = 1 (mod p) has to have the smallest non-zero solution m = phi(p).

Asssume there exists n < phi(p) such that h^n = 1 (mod p), and n is minimal.
The powers of h generate a subgroup of size n. From Lagrange's theorem, we know that the size of the subgroup must divide the size of the parent group `Z_p*`.

Since `|z_p*| = phi(p)`, n divides phi(p). This means that `d = phi(p)/n` is a divisor of phi(p). Conversely, `n = phi(p)/d`
Knowing that n < phi(p), then d > 1.

Looking back at the equation satisfied by n:
```
h^n = h^(phi(p)/d) = 1 (mod p)
```

This means that h is a dth power residue, which contradicts with the hypothesis.
So, we can say that the smallest m such that h^m = 1 (mod p) is phi(p). In conclusion, h is a generator of `Z_p*`.  

```
g^m = g^0 (mod p)
m = 0 (mod phi(p))
```

---

# The number of generators modulo p is phi(phi(p)).

We can prove this by using the last two lemmas.

## Upper bound

The first lemma gives us an upper bound:
> If g is an dth power residue modulo p, for a divisor d > 1 of phi(p), g can't be a generator
Using its negation:
> If g is a generator, then g is not a dth power residue modulo p, for any divisor d > 1 of phi(p)

Let h be a generator. Then {h^0, h^1, ..., h^phi(p)} is `Z_p*`.

Assume gcd(m, phi(p)) = d. d > 1, and m = k * d, for some integer k.
```
h^m = = h^(k*d) = (h^k)^d (mod p)
```
Which means that h^m is a dth power residue. The number of such m's, for d > 1,
is exactly phi(p) - phi(phi(p)). That's because phi(phi(p)) counts the numbers
m for which gcd(m, phi(p)) = 1.

So, we know that out of phi(p), phi(p) - phi(phi(p)) numbers in `Z_p*` can't
be generators.

```
number of generators <= phi(phi(p))
```

## Lower bound

Using the second lemma:
> If, for any divisor d > 1 of phi(p), h is not a dth power residue mod p, then h is a generator, for p > 2

Again, taking a generator h, and looking at {h^0, ..., h^phi(p)}, if h^m is not
a power residue, we can say that gcd(m, phi(p)) = 1.
Then, h^m is a generator. The amount of numbers m such that gcd(m, phi(p)) = 1 is phi(phi(p)).

````
phi(phi(p)) <= number of generators
```

## Conclusion

Using the 2 bounds, we can conclude that the number of generators is phi(phi(p)).

A next result that a found, but didn't have time to prove, is that there are phi(o) numbers that have the order o, in the group Z_p*.
