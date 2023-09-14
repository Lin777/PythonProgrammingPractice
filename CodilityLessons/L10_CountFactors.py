"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
def solution(N):
    factors = 2 # add 1 because the number is factor of itself and another one because is all numbers are factors of 1
    for i in range(2,N//2+1):
        if N%i == 0:
            factors += 1
    return factors

def solution(N):
    i = 1
    result = 0
    while (i*i < N):
        if (N % i == 0):
            result += 2
        i += 1
    if (i*i == N):
        result +=1
    return result

print(solution(24))
print(solution(10))
