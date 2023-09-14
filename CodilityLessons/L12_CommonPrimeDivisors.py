"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of arrays A and B is an integer within the range [1..2,147,483,647].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

"""
goal -> check whether the sets of primes divisors of integers N and M  are exactly the sema
N=15 and M = 75 -> prime divisors are the same: {3,5}
N=10 and M=30 -> aren't the same: {2,5} != {2,3,5}
n=9 and M=5 -> aren't the same: {3} != {5}
any number can be written into prime numbers factors! 10 =2 * 5 , 112 = (2**4)*7
The GCD (gratest common divisor) of 2 numbers is also made of the common prime numbers: between 10 and 112 -> 2
Find the prime factor that is not common to both numbers
M' = M/GCD(M,N) = 5 ^ 2
M'' = M' / GCD(M',N) = 5
M''' = M''/GCD(M'',N) = 1 --> when they don't have the same prime numbers, the last N''' != 1
is the same as the last N''
"""

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def solution(A,B):
    l = len(A)
    cnt = 0
    for i in range(0,l):
        a = A[i]
        b = B[i]
        D = gcd(a,b)
        while (gcd(a,D) != 1):
            a /= gcd(a,D)
        while (gcd(b, D) != 1):
            b /= gcd(b, D)
        if (a==1 and b==1):
            cnt  += 1
    return cnt

A = [15,10,3]
B = [75,30,5]
print(solution(A,B)) # 1 only one pair (15,75)


