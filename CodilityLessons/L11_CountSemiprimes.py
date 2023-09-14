"""

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P and Q is an integer within the range [1..N];
P[i] ≤ Q[i].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""

"""
semi prime= product of two prime numbers
"""

def solution(N,P,Q):
    """
    primes -> number q for prime numbers
    semiprimes -> number 1 for semiprimes
    semiprimescum -> sum of semiprimes up to a certain position
    :param A:
    :return:
    """
    primes = [1] * (N+1)
    primes[0] = primes[1] = 0
    for i in range(2, int(N**(1/2))+1):
        if primes[i]:
            k = i*i
            while k<=N:
                primes[k]=0
                k += i
    allsemiprimes = [0] * (N+1)
    for i in range(0, N+1):
        for j in range(0, N+1):
            if primes[i] and primes[j] and i*j<=N:
                allsemiprimes[i*j] = 1
            if i*j > N:
                break
    semiprimes = [0] *len(P)
    semiprimescum = [0] * (N+1)
    s = 0

    for i in range(0, N+1):
        s += allsemiprimes[i]
        semiprimescum[i] = s

    for i in range(0, len(P)):
        semiprimes[i] = semiprimescum[Q[i]] - semiprimescum[P[i]-1]
    return semiprimes

P = [1,4,16]
Q = [26,10,20]

print(solution(30, P,Q)) # [10,4,0]
