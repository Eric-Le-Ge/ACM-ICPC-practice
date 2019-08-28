'''
Source: https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/
'''

# Python3 program to find prime factorization  
# of a number n in O(Log n) time with  
# precomputation allowed. 
import math as mt 
from collections import Counter
  
MAXN = 1000001
  
# stores smallest prime factor for 
# every number 
spf = [0 for i in range(MAXN)] 
  
# Calculating SPF (Smallest Prime Factor)  
# for every number till MAXN. 
# Time Complexity : O(nloglogn) 
def sieve(): 
    spf[1] = 1
    for i in range(2, MAXN): 
          
        # marking smallest prime factor  
        # for every number to be itself. 
        spf[i] = i 
  
    # separately marking spf for  
    # every even number as 2 
    for i in range(4, MAXN, 2): 
        spf[i] = 2
  
    for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
          
        # checking if i is prime 
        if (spf[i] == i): 
              
            # marking SPF for all numbers 
            # divisible by i 
            for j in range(i * i, MAXN, i):  
                  
                # marking spf[j] if it is  
                # not previously marked 
                if (spf[j] == j): 
                    spf[j] = i 
  
# A O(log n) function returning prime  
# factorization by dividing by smallest  
# prime factor at every step 
def getFactorization(x): 
    ret = list() 
    while (x != 1): 
        ret.append(spf[x]) 
        x = x // spf[x] 
  
    return ret 
  
sieve() 
# This code is contributed  
# by Mohit kumar 29 

T = int(input())
for t in range(1, T+1):

    l, r = [int(_) for _ in input().split()]
    res = 0
    if l==1:
        res += 1
        l += 1
    for num in range(l, r+1):
        facs = getFactorization(num)
        twos = facs.count(2)
        odds = len(facs)-twos + 1
        if odds>2:
            if twos==1:
                res += 1
        elif odds==2:
            if twos<3:
                res += 1
        else:
            if twos<4:
                res += 1
        
        
    print ("Case #{}: {}".format(t, res))










