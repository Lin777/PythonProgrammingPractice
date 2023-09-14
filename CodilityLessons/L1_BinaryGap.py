"""
# Binary Gap

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at
both ends in the binary representation of N.

For example,
The number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps.
The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its
 longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation
 '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].

Copyright 2009–2023 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""
"""def solution(X, A):
    list_journey = [-1] * X
    for i, v in enumerate(A):
        if v <= X:
            if list_journey[v-1]<0:
                list_journey[v-1] = i
    if min(list_journey) == -1:
        return -1
    else:
        return max(list_journey)"""

def solution(N):
    binary_number = str(bin(N))[2:]
    max_gap = 0
    count_zeros = 0
    for num in binary_number:
        if num == '0':
            count_zeros += 1
        elif num == '1':
            max_gap = max(count_zeros, max_gap)
            count_zeros = 0
    return max_gap

print(solution(9)) #2
print(solution(529)) #4, 3 ->4
print(solution(20)) #1
print(solution(15)) #0
print(solution(32)) #0