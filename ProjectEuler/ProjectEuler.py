import memoize
from math import sqrt

def divisors(n) : 
    divisors = []  
    for i in range(1,int(sqrt(n)+1)):           
        if (n%i==0) :
            d = n//i
            if (n//i==i) : 
                divisors.append(i)
            else : 
                divisors.append(i)
                divisors.append(n//i) 
    return sorted(divisors)

def memoize(func):
    cache = dict()
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoized_func

def triang2(n):
    return int(n*(n+1)/2)
    
def triang(n):
    '''Generate n-th triangular number'''
    if n==0:
        return 0
    if n==1:
        return 1
    return triang(n-1) + n

triangmem = memoize(triang)

def fib(n):
    '''Generate n-th Fibonacci number'''
    if n==1:
        return 1
    if n==2:
        return 2
    return fib(n-1) + fib(n-2)

fibmem = memoize(fib)

def primeFactors(n):
    """Returns all prime factors of a positive integer. Returns n if prime"""
    factors = []
    d = 2 # begin by attempting to divide by 2
    while n > 1:
        while n % d == 0: # check if I can divide n by d, if so store factor and repeat with quotient
            factors.append(d)
            n /= d
        d = d + 1 # increase divident
    return factors

def yieldFactors(n):
    i = 2
    while i*i<=n:
        if n%i == 0:
            n/=i
            yield i
        else:
            i+=1
    if n>1:
        yield int(n)

#def isPrime(n):
#    f = primeFactors(n)
#    if len(f)!=1:
#        return False
#    else:
#        return True

def isPrime(n):
    if n == 1:
        return False
    i = 2
    # loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # n has a factor in between 2 and sqrt(n), so it is not a prime
            return False
        i += 1
    return True

isPrime_mem = memoize(isPrime)


# Miller–Rabin primality test
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def isPrimeMR(n, k=3):
    import random
    if n < 6:  # assuming n >= 0 in all cases shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n % 2 == 0:  # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        for a in random.sample(range(2, n-2), k):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    elif x == n - 1:
                        a = 0
                        break
                    if a:
                        return False
        return True


def factors(n):
    """Returns all factors of a positive integer. Returns n if prime"""
    factors = []
    for i in range(1, n + 1):
       if n % i == 0:
           factors.append(i)
    return factors

# https://stackoverflow.com/questions/567222/simple-prime-generator-in-python

def generatePrimes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1


# Generate Pythagorean Triple accoding to
# https://mathworld.wolfram.com/PythagoreanTriple.html

import numpy as np

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)

def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim            
