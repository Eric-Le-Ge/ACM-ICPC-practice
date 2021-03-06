
def gcd(a, b) :
    if (a == 0) :
        return b
    return gcd(b % a, a)

# To compute x^y under modulo m
def power(x, y, m) :
    if (y == 0) :
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
    if(y % 2 == 0) :
        return p
    else :
        return ((x * p) % m)

#m must be prime
def inv(a, m) :
    return power(a, m - 2, m)

#m does not need to be prime
def inv(a, m) : 
    m0, x0, x1 = m , 0, 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        q = a // m 
        t = m
        m = a % m 
        a = t 
        t = x0 
        x0 = x1 - q * x0 
        x1 = t 
    if (x1 < 0) : 
        x1 = x1 + m0 
    return x1 

# https://stackoverflow.com/questions/3025162/statistics-combinations-in-python/3027128
def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

''' Chinese remainder Theorem
num: [int] defining mods. Must be coprime.
rem: remainder for each mod

depends on inv: choose which one to use based on fact if nums are prime
'''
def crt(num, rem):
    k = len(num)
    prod = 1
    for i in range(k):
        prod *= num[i]
    result = 0
    for i in range(k):
        pp = prod // num[i]
        result += rem[i] * inv(pp, num[i]) * pp;
    return result % prod;

